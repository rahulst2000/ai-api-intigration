import os

import cohere
from dotenv import load_dotenv

# API Configuration
load_dotenv()

api_key = os.getenv("COHERE_API_KEY")
client = cohere.Client(api_key) if api_key else None


def query_api(prompt):
    """Query the Cohere API with a prompt."""
    try:
        if not api_key:
            return "Error: COHERE_API_KEY is not set."
        response = client.chat(
            model="command-r-08-2024",
            message=prompt,
            max_tokens=500,
            temperature=0.7,
        )
        return response.text.strip()
    except Exception as error:
        return f"Error: {error!r}"


# Main Execution
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying API...")
    result = query_api(user_prompt)
    print("Response:")
    print(result)
