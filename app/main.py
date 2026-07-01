from fastapi import FastAPI

from app.routes.chat import router as chat_router
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
)

app.include_router(chat_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the AI Chat API!"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}