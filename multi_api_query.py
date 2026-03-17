import os

import cohere
from dotenv import load_dotenv
from google import genai
from groq import Groq
from huggingface_hub import InferenceClient
from huggingface_hub.errors import HfHubHTTPError

load_dotenv()


def build_clients():
    """Create provider clients only when the matching API key exists."""
    groq_api_key = os.getenv("GROQ_API_KEY")
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    cohere_api_key = os.getenv("COHERE_API_KEY")
    huggingface_api_key = os.getenv("HUGGINGFACE_API_KEY")

    return {
        "Groq": Groq(api_key=groq_api_key) if groq_api_key else None,
        "Gemini": genai.Client(api_key=gemini_api_key) if gemini_api_key else None,
        "Cohere": cohere.Client(cohere_api_key) if cohere_api_key else None,
        "Hugging Face": (
            InferenceClient(provider="auto", api_key=huggingface_api_key)
            if huggingface_api_key
            else None
        ),
    }


CLIENTS = build_clients()


def query_groq(prompt):
    client = CLIENTS["Groq"]
    if not client:
        return "Error: GROQ_API_KEY is not set."

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as error:
        return f"Error: {error}"


def query_gemini(prompt):
    client = CLIENTS["Gemini"]
    if not client:
        return "Error: GEMINI_API_KEY is not set."

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        return response.text
    except Exception as error:
        return f"Error: {error}"


def query_cohere(prompt):
    client = CLIENTS["Cohere"]
    if not client:
        return "Error: COHERE_API_KEY is not set."

    try:
        response = client.chat(
            model="command-r-08-2024",
            message=prompt,
            max_tokens=500,
            temperature=0.7,
        )
        return response.text.strip()
    except Exception as error:
        return f"Error: {error}"


def query_huggingface(prompt):
    client = CLIENTS["Hugging Face"]
    if not client:
        return "Error: HUGGINGFACE_API_KEY is not set."

    try:
        response = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V3-0324",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7,
        )
        return response.choices[0].message.content
    except HfHubHTTPError as error:
        if "403" in str(error) and "Inference Providers" in str(error):
            return (
                "Error: Your HUGGINGFACE_API_KEY does not have permission to use "
                "Hugging Face Inference Providers."
            )
        if "404" in str(error):
            return "Error: The selected Hugging Face model is unavailable."
        return f"Error: {error}"
    except Exception as error:
        return f"Error: {error}"


def main():
    prompt = input("Enter your prompt: ")

    providers = [
        ("GROQ RESPONSE", query_groq),
        ("GEMINI RESPONSE", query_gemini),
        ("COHERE RESPONSE", query_cohere),
        ("HUGGINGFACE RESPONSE", query_huggingface),
    ]

    for title, query_fn in providers:
        print(f"\n--- {title} ---")
        print(query_fn(prompt))


if __name__ == "__main__":
    main()
