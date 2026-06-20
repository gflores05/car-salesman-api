from collections.abc import AsyncIterable

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse

from .car_salesman import send_query
from .customer import Customer

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
async def ask(customer: Customer) -> AsyncIterable[str | None]:
  try:
    for chunk in send_query(customer):
      yield chunk.text
  except Exception:
    yield "We are experimenting some issues for now. Please try again later."
