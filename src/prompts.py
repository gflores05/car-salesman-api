from langchain_core.prompts import (
  ChatPromptTemplate,
  HumanMessagePromptTemplate,
  MessagesPlaceholder,
  SystemMessagePromptTemplate,
)

SYSTEM_PROMPT = SystemMessagePromptTemplate.from_template(
  "Your name is Gabriel. You're a car salesperson in {country} with several years of experience. Your job is to help people choose the car that best suits them based on the parameters of marital status, age, nationality, and salary. Respond casually, in the language of the country and with the characteristic way of speaking of that country."
)

QUESTIONS_PROMPT = HumanMessagePromptTemplate.from_template(
  """First, we need to greet the customer in their language and let them know we are here to help them choose their ideal car. Return the text for this initial greeting.
  "Also, to obtain the parameters required to determine the best car options for a person, we need to ask them a few questions in their own language. Return the questions for each parameter"""
)

CAR_RECOMMENDATION_PROMPT = HumanMessagePromptTemplate.from_template(
  "What's the best car for me based on my responses? Return the result as markdown and in the language of the country."
)


def create_question_prompt():
  return ChatPromptTemplate.from_messages([SYSTEM_PROMPT, QUESTIONS_PROMPT])


def create_recommendation_prompt():
  return ChatPromptTemplate.from_messages(
    [
      SYSTEM_PROMPT,
      MessagesPlaceholder(variable_name="history"),
      CAR_RECOMMENDATION_PROMPT,
    ]
  )
