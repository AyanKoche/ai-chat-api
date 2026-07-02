from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    prompt: str = Field(
        ...,
        min_length=1,
        max_length=1000,
        description="The prompt to send to the LLM",
        examples=["What is the capital of India?"],
    )

class ChatResponse(BaseModel):
    response: str