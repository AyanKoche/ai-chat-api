from fastapi import FastAPI

from app.routes.chat import router as chat_router

app = FastAPI(
    title="AI Chat API",
    version="1.0.0",
    description="A production-style AI backend built with FastAPI and Ollama."
)

app.include_router(chat_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the AI Chat API!"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}