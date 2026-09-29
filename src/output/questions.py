from pydantic import BaseModel, Field


class QuestionsOutputModel(BaseModel):
  greet: str = Field(description="The initial greeting in the client's language")
  name_question: str = Field(
    description="The question to ask the client for their name"
  )
  age_question: str = Field(description="The question to ask the client for their age")
  salary_question: str = Field(
    description="The question to ask the client for their salary"
  )
  marital_status_question: str = Field(
    description="The question to ask the client for their marital status"
  )
