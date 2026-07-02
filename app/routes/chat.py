from fastapi import APIRouter
from pydantic import BaseModel

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.ollama_service import ask_llm
from app.core.logging import logger

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    logger.info(f"Chat request received: {request.prompt}")
    answer = await ask_llm(request.prompt)
    logger.info(f"Chat response sent: {answer}")
    return ChatResponse(response=answer)