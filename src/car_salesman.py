import os
import time
from typing import Iterator

from dotenv import load_dotenv
from google import genai
from google.genai.errors import APIError

from .customer import Customer

# Load the variables from the .env file
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def get_response(
  prompt: str, country: str, max_retries=5, initial_delay=2
) -> Iterator[genai.types.GenerateContentResponse]:
  delay = initial_delay
  for attempt in range(max_retries):
    try:
      return client.models.generate_content_stream(
        model="gemini-3.5-flash",
        contents=prompt,
        config=genai.types.GenerateContentConfig(
          system_instruction=f"You are a car salesman from {country}. Respond in the language of the country and with the characteristic way of speaking of that country."
        ),
      )
    except APIError as e:
      if e.code == 503:
        print(
          f"Attempt {attempt + 1} failed due to 503 (High Demand). Retrying in {delay}s."
        )
        time.sleep(delay)
        delay *= 2
      else:
        raise e
    except Exception as e:
      print(f"Non-retryable error: {e}")
      raise e

  raise Exception("Max retries exceeded. Gemini API is still unavailable.")


def generate_prompt(params: Customer) -> str:
  budget_prompt = (
    f"my monthly budget is ${params.budget}" if params.budget is not None else None
  )
  salary_prompt = (
    f"my montly salary is ${params.salary}" if params.salary is not None else None
  )

  return f"""
What's the best car for me if I'm {params.marital_status}, I'm {params.age} years old, I'm from {params.country}
{"and " if budget_prompt is not None or salary_prompt is not None else ""} {budget_prompt or salary_prompt or ""}
"""


def send_query(params: Customer):
  prompt = generate_prompt(params)

  return get_response(prompt=prompt, country=params.country)
