from pydantic_settings import BaseSettings, SettingsConfigDict

from src.types import ChatService


class Settings(BaseSettings):
  app_name: str = "Car Salesman"
  openai_api_key: str = "xxxx"
  gemini_api_key: str = "xxxx"
  ollama_base_url: str = "http://localhost:11434"
  chat_service: ChatService = "openai"
  ai_model: str = "gpt-4o-mini"
  temperature: float = 0.7
  model_config = SettingsConfigDict(env_file=".env")


def settings_factory() -> Settings:
  return Settings()
