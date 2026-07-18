import httpx

from app.core.config import settings
from app.core.logging import logger
from app.exceptions.ollama import OllamaConnectionError, OllamaResponseError

OLLAMA_URL = f"{settings.ollama_url}/api/generate"
MODEL_NAME = settings.ollama_model

async def chat(message: str):
    try:
        async with httpx.AsyncClient(timeout=60) as client:
            response = await client.post(
                OLLAMA_URL,
                json={
                    "model": MODEL_NAME,
                    "message": message,
                    "stream": False,
                },
                timeout=60,
            )
    except httpx.TimeoutException as e:
        raise OllamaConnectionError(f"Timeout while connecting to the Ollama API: {e}") from e
    except httpx.RequestError as e:
        raise OllamaConnectionError(f"Request error while connecting to the Ollama API: {e}") from e
    
    if response.status_code == 500:
        raise OllamaResponseError("Received an error response from the Ollama API")
    elif response.status_code != 200:
        raise OllamaConnectionError("Failed to connect to the Ollama API")

    data = response.json()
    logger.info(f"LLM response: {data['response']}")
    return data["response"]

async def stream_chat(message: str):
    async with httpx.AsyncClient(timeout=None) as client:
        async with client.stream(
            "POST",
            f"{settings.ollama_url}/api/chat",
            json={
                "model": settings.ollama_model,
                "messages": [{"role": "user", "content": message}],
                "stream": True,
            },
        ) as response:
            response.raise_for_status()
            async for line in response.aiter_text():
                if line:
                    yield line +"\n"
