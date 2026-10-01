from typing import Annotated

from fastapi import Depends
from langchain.messages import AIMessage, HumanMessage

from src.input.car_recommendation import CarRecommendationInputModel
from src.prompts import create_recommendation_prompt
from src.services.ai_base_service import AIBaseService
from src.settings import Settings, settings_factory


class CarSalesmanService(AIBaseService):
  def __init__(self, settings: Settings) -> None:
    super().__init__(settings)

  def _create_chain(self):
    model = self._create_chat()

    chat_prompt = create_recommendation_prompt()

    return chat_prompt | model

  def _get_messages_history(self, input: CarRecommendationInputModel):
    return [
      AIMessage(content=input.greet),
      AIMessage(content=input.name.question),
      HumanMessage(content=input.name.answer),
      AIMessage(content=input.country.question),
      HumanMessage(content=input.country.answer),
      AIMessage(content=input.age.question),
      HumanMessage(content=str(input.age.answer)),
      AIMessage(content=input.marital_status.question),
      HumanMessage(content=input.marital_status.answer),
      AIMessage(content=input.salary.question),
      HumanMessage(content=str(input.salary.answer)),
    ]

  def get_recommendations(self, input: CarRecommendationInputModel):
    chain = self._create_chain()

    return chain.stream(
      {"history": self._get_messages_history(input), "country": input.country.answer}
    )


def car_salesman_service_factory(
  settings: Annotated[Settings, Depends(settings_factory)],
) -> CarSalesmanService:
  return CarSalesmanService(settings=settings)
