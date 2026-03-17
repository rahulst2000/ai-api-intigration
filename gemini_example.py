import os

from dotenv import load_dotenv
from google import genai

# API Configuration
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None


def query_api(prompt):
    """Query the Gemini API with a prompt."""
    try:
        if not api_key:
            return "Error: GEMINI_API_KEY is not set."
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        return response.text
    except Exception as error:
        return f"Error: {error}"


# Main Execution
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying API...")
    result = query_api(user_prompt)
    print("Response:")
    print(result)
