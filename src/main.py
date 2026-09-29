from collections.abc import AsyncIterable
from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from langsmith import BadRequestError, RateLimitError

from src.input.car_recommendation import CarRecommendationInputModel
from src.input.questions import QuestionsInputModel
from src.output.questions import QuestionsOutputModel
from src.services.car_salesman_service import (
  CarSalesmanService,
  car_salesman_service_factory,
)
from src.services.questions_service import QuestionsService, questions_service_factory

app = FastAPI()

origins = [
  "http://localhost",
  "http://localhost:4200",
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)


@app.post("/ask", response_class=StreamingResponse)
async def ask(
  input: CarRecommendationInputModel,
  car_salesman_service: Annotated[
    CarSalesmanService, Depends(car_salesman_service_factory)
  ],
) -> AsyncIterable[str | None]:

  try:
    for chunk in car_salesman_service.get_recommendations(input):
      yield chunk.text
  except BadRequestError:
    yield "Invalid request"
  except RateLimitError:
    yield "We are experimenting some issues for now. Please try again later."


@app.post("/questions", response_model=QuestionsOutputModel)
async def questions(
  input: QuestionsInputModel,
  questions_service: Annotated[QuestionsService, Depends(questions_service_factory)],
) -> QuestionsOutputModel:
  return questions_service.get_questions(input)
