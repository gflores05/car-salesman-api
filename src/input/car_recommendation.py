from pydantic import BaseModel

from src.types import Country, MaritalStatus


class CarRecommendationInputModel(BaseModel):
  age: int
  marital_status: MaritalStatus
  country: Country
  salary: float
