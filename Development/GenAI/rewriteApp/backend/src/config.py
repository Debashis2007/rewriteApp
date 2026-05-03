"""Configuration management for the backend."""

from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    """Application settings from environment variables."""

    # LLM Configuration
    openai_api_key: str = ""
    openai_model: str = "gpt-4-turbo-preview"
    anthropic_api_key: str = ""
    anthropic_model: str = "claude-3-opus-20240229"
    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "llama2"
    llm_provider: str = "ollama"
    llm_model: str = "llama2"

    # Logging
    log_level: str = "INFO"
    json_logging: bool = True

    # System
    debug: bool = False
    port: int = 8000
    cors_origins: List[str] = [
        "http://localhost:3000",
        "http://localhost:8080",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:8080",
        "*",
    ]

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
