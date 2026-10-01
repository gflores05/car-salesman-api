from pydantic import BaseModel

from src.types import Country, MaritalStatus


class QuestionAnswerInputModel[T](BaseModel):
  question: str
  answer: T


class CarRecommendationInputModel(BaseModel):
  greet: str
  name: QuestionAnswerInputModel[str]
  age: QuestionAnswerInputModel[int]
  marital_status: QuestionAnswerInputModel[MaritalStatus]
  country: QuestionAnswerInputModel[Country]
  salary: QuestionAnswerInputModel[float]
