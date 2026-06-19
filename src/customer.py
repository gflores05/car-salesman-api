from typing import Optional

from pydantic import BaseModel, Field

from .types import Country, MaritalStatus


class Customer(BaseModel):
  age: int
  marital_status: MaritalStatus
  country: Country
  salary: Optional[float] = Field(default=None, description="The montly salary")
  budget: Optional[float] = Field(default=None, description="The montly budget")
