from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import StreamingResponse

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.ollama_service import chat, stream_chat
from app.core.logging import logger

router = APIRouter()

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    logger.info(f"Chat request received: {request.message}")
    answer = await chat(request.message)
    logger.info(f"Chat response sent: {answer}")
    return ChatResponse(response=answer)

@router.post("/chat/stream")
async def stream_chat_endpoint(request: ChatRequest):
    return StreamingResponse(stream_chat(request.message), media_type="application/x-ndjson",)