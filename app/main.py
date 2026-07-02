from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.routes.chat import router as chat_router
from app.core.config import settings
from app.core.logging import logger
from app.exceptions.ollama import OllamaConnectionError, OllamaResponseError

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

app.include_router(chat_router)

@app.get("/")
async def root():
    logger.info("Root endpoint accessed")
    return {"message": "Welcome to the AI Chat API!"}


@app.get("/health")
async def health_check():
    logger.info("Health check endpoint accessed")
    return {"status": "healthy"}

@app.exception_handler(OllamaConnectionError)
async def handle_connection_error(request: Request, exc: OllamaConnectionError):
    logger.error(f"OllamaConnectionError: {exc}")
    return JSONResponse(status_code=503, content={"error": "Failed to connect to the Ollama API. Please try again later."})

@app.exception_handler(OllamaResponseError)
async def handle_response_error(request: Request, exc: OllamaResponseError):
    logger.error(f"OllamaResponseError: {exc}")
    return JSONResponse(status_code=500, content={"error": "Received an error response from the Ollama API. Please try again later."})