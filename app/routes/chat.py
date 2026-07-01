from fastapi import APIRouter
from pydantic import BaseModel

from app.services.ollama_service import ask_llm

router = APIRouter()

class ChatRequest(BaseModel):
    prompt: str

@router.post("/chat")
async def chat(request: ChatRequest):
    answer = await ask_llm(request.prompt)
    return {"response": answer}