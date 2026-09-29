from pydantic import BaseModel

from src.types import Country


class QuestionsInputModel(BaseModel):
  country: Country
