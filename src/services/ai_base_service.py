from langchain.chat_models import BaseChatModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI

from src.settings import Settings


class ModelNotImplementedException(BaseException):
  def __init__(self, *args: object) -> None:
    super().__init__(*args)


class AIBaseService:
  def __init__(self, settings: Settings) -> None:
    self.settings = settings

  def _create_chat(self) -> BaseChatModel:
    match self.settings.chat_service:
      case "openai":
        return ChatOpenAI(
          model=self.settings.ai_model, temperature=self.settings.temperature
        )
      case "gemini":
        return ChatGoogleGenerativeAI(
          model=self.settings.ai_model, temperature=self.settings.temperature
        )
      case "ollama":
        return ChatOllama(
          model=self.settings.ai_model,
          base_url=self.settings.ollama_base_url,
          temperature=self.settings.temperature,
        )

    raise ModelNotImplementedException()
