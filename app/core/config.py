from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "AI Chat API"
    app_version: str = "1.0.0"

    ollama_url: str = "http://localhost:11434"
    ollama_model: str = "qwen2.5:3b"

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()