from typing import Annotated

from fastapi import Depends

from src.input.car_recommendation import CarRecommendationInputModel
from src.prompts import create_recommendation_prompt
from src.services.ai_base_service import AIBaseService
from src.settings import Settings, settings_factory


class CarSalesmanService(AIBaseService):
  def __init__(self, settings: Settings) -> None:
    super().__init__(settings)

  def _create_chain(self):
    model = self._create_chat()

    prompt = create_recommendation_prompt()

    return prompt | model

  def get_recommendations(self, input: CarRecommendationInputModel):
    chain = self._create_chain()

    return chain.stream(input.model_dump())


def car_salesman_service_factory(
  settings: Annotated[Settings, Depends(settings_factory)],
) -> CarSalesmanService:
  return CarSalesmanService(settings=settings)
