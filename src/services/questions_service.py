from typing import Annotated

from fastapi import Depends

from src.input.questions import QuestionsInputModel
from src.output.questions import QuestionsOutputModel
from src.prompts import create_question_prompt
from src.services.ai_base_service import AIBaseService
from src.settings import Settings, settings_factory


class QuestionsService(AIBaseService):
  def __init__(self, settings: Settings) -> None:
    super().__init__(settings)

  def _create_chain(self):
    base_model = self._create_chat()

    structured_model = base_model.with_structured_output(QuestionsOutputModel)

    prompt = create_question_prompt()

    return prompt | structured_model

  def get_questions(self, input: QuestionsInputModel) -> QuestionsOutputModel:
    chain = self._create_chain()

    result = chain.invoke(input.model_dump())

    if isinstance(result, QuestionsOutputModel):
      return result
    return QuestionsOutputModel.model_validate(result)


def questions_service_factory(
  settings: Annotated[Settings, Depends(settings_factory)],
) -> QuestionsService:
  return QuestionsService(settings)
