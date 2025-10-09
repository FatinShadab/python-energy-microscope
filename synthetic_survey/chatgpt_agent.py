# File: chatgpt.py

import os
import json
import time
from openai import OpenAI
from pydantic import ValidationError
import random

# Import the common Pydantic model and utility functions
from utils import SurveyResponse, SURVEY_PROMPT, save_to_csv

MODEL_NAME = "gpt-4o-mini"
OUTPUT_FILENAME = "synthetic_survey_responses_chatgpt.csv"
NUM_RESPONSES = 50  # Number of rows to generate


def generate_chatgpt_response(client):
    """Generates a single synthetic survey response using the OpenAI API with JSON mode."""
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a sophisticated JSON generator. "
                    "Your only output must be a single, valid JSON object "
                    "that strictly conforms to the following Pydantic schema description. "
                    "Do not include any other text, formatting, or markdown wrappers (like ```json). "
                    f"Schema: {SurveyResponse.model_json_schema()}"
                ),
            },
            {"role": "user", "content": SURVEY_PROMPT},
        ],
        response_format={"type": "json_object"},
        temperature=random.uniform(0.5, 0.9)  # Slight randomness for diversity
    )

    raw_json = response.choices[0].message.content

    # Validate JSON against schema
    validated_data = SurveyResponse.model_validate_json(raw_json)
    return validated_data.model_dump()


def generate_multiple_responses():
    """Generates multiple synthetic survey responses and saves them to CSV."""
    print(f"Generating {NUM_RESPONSES} synthetic survey responses using {MODEL_NAME}...\n")

    try:
        client = OpenAI(api_key="api-key")
    except Exception as e:
        print(f"Error initializing OpenAI client: {e}")
        print("Please ensure your OPENAI_API_KEY environment variable is set.")
        return

    success_count = 0
    for i in range(NUM_RESPONSES):
        try:
            print(f"→ Generating response {i + 1}/{NUM_RESPONSES}...", end=" ", flush=True)
            response_dict = generate_chatgpt_response(client)
            save_to_csv(response_dict, OUTPUT_FILENAME)
            success_count += 1
            print("✅ Saved.")
            time.sleep(1)  # polite delay to avoid rate limits

        except ValidationError as e:
            print(f"\n❌ Validation error on response {i + 1}: {e}")
            continue
        except Exception as e:
            print(f"\n⚠️ Error on response {i + 1}: {e}")
            continue

    print(f"\n✅ Completed! Successfully generated {success_count}/{NUM_RESPONSES} valid responses.")
    print(f"Saved to: {OUTPUT_FILENAME}")


if __name__ == "__main__":
    generate_multiple_responses()
