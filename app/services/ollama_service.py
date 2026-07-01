import httpx

OLLAMA_URL = "http://localhost:11434/api/generate"

async def ask_llm(prompt: str):
    async with httpx.AsyncClient(timeout=60) as client:
        response = await client.post(
            OLLAMA_URL,
            json={
                "model": "qwen2.5:3b",
                "prompt": prompt,
                "stream": False,
            },
        )

    response.raise_for_status()

    data = response.json()
    return data["response"]