import httpx

from app.core.config import settings
from app.core.logging import logger

OLLAMA_URL = f"{settings.ollama_url}/api/generate"
MODEL_NAME = settings.ollama_model

async def ask_llm(prompt: str):
    async with httpx.AsyncClient(timeout=60) as client:
        response = await client.post(
            OLLAMA_URL,
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False,
            },
        )

    response.raise_for_status()

    data = response.json()
    logger.info(f"LLM response: {data['response']}")
    return data["response"]