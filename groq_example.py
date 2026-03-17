import os

from dotenv import load_dotenv
from groq import Groq

# API Configuration
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key) if api_key else None


def query_api(prompt):
    """Query the Groq API with a prompt."""
    try:
        if not api_key:
            return "Error: GROQ_API_KEY is not set."
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as error:
        return f"Error: {error}"


# Main Execution
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying API...")
    result = query_api(user_prompt)
    print("Response:")
    print(result)
