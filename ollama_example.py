import os

import ollama
from dotenv import load_dotenv

# API Configuration
load_dotenv()

ollama_host = os.getenv("OLLAMA_HOST")
ollama_api_key = os.getenv("OLLAMA_API_KEY")

client_kwargs = {}
if ollama_host:
    client_kwargs["host"] = ollama_host
if ollama_api_key:
    client_kwargs["headers"] = {"Authorization": f"Bearer {ollama_api_key}"}

client = ollama.Client(**client_kwargs)


def query_api(prompt):
    """Query the Ollama API with a prompt."""
    try:
        response = client.generate(
            model="llama3",
            prompt=prompt,
            options={"temperature": 0.7},
        )
        return response["response"]
    except Exception as error:
        return f"Error: {error}"


# Main Execution
if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    print("Querying API...")
    result = query_api(user_prompt)
    print("Response:")
    print(result)
