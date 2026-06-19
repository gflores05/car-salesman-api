from collections.abc import AsyncIterable

from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from .car_salesman import send_query
from .customer import Customer

app = FastAPI()


@app.post("/ask", response_class=StreamingResponse)
async def ask(customer: Customer) -> AsyncIterable[str | None]:
  for chunk in send_query(customer):
    yield chunk.text
