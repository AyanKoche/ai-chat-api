from fastapi import APIRouter
from pydantic import BaseModel

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.ollama_service import ask_llm

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    answer = await ask_llm(request.prompt)
    return ChatResponse(response=answer)