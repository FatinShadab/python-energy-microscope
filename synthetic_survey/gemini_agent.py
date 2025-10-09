# File: gemini_multiple.py

import os
import time
import random
from google import genai
from google.genai import types
from pydantic import ValidationError

# Import the common Pydantic model and utility functions
from utils import SurveyResponse, SURVEY_PROMPT, save_to_csv 

MODEL_NAME = "gemini-2.5-flash"
OUTPUT_FILENAME = "synthetic_survey_responses_gemini.csv"
NUM_RESPONSES = 50  # Number of rows to generate


def generate_gemini_response(client):
    """Generates a single synthetic survey response using the Gemini API."""
    try:
        config = types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=SurveyResponse,
            temperature=random.uniform(0.5, 0.9)  # Slight randomness for diversity
        )

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=SURVEY_PROMPT,
            config=config
        )

        # Validate and parse Pydantic object
        if response.parsed and isinstance(response.parsed, SurveyResponse):
            return response.parsed.model_dump()
        else:
            print("\n❌ Error: Model response not in the expected structured format.")
            print("Raw model text response (for debugging):")
            print(getattr(response, "text", "No text available"))
            return None

    except ValidationError as e:
        print(f"\n❌ Validation error: {e}")
        return None
    except Exception as e:
        print(f"\n⚠️ Error during Gemini API call: {e}")
        return None


def generate_multiple_responses():
    """Generates multiple synthetic survey responses and saves them to CSV."""
    print(f"Generating {NUM_RESPONSES} synthetic survey responses using {MODEL_NAME}...\n")

    try:
        client = genai.Client(api_key="api-key")  # Replace with actual key
    except Exception as e:
        print(f"Error initializing Gemini client: {e}")
        print("Please ensure your GEMINI_API_KEY environment variable is set.")
        return

    success_count = 0
    for i in range(NUM_RESPONSES):
        print(f"→ Generating response {i + 1}/{NUM_RESPONSES}...", end=" ", flush=True)
        response_dict = generate_gemini_response(client)
        if response_dict:
            save_to_csv(response_dict, OUTPUT_FILENAME)
            success_count += 1
            print("✅ Saved.")
        else:
            print("❌ Skipped due to error.")

        time.sleep(1)  # polite delay to avoid rate limits

    print(f"\n✅ Completed! Successfully generated {success_count}/{NUM_RESPONSES} valid responses.")
    print(f"Saved to: {OUTPUT_FILENAME}")


if __name__ == "__main__":
    generate_multiple_responses()
