import os
import sys

from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from huggingface_hub.errors import HfHubHTTPError

# API Configuration
load_dotenv()

api_key = os.getenv("HUGGINGFACE_API_KEY")
client = (
    InferenceClient(
        provider="auto",
        api_key=api_key,
    )
    if api_key
    else None
)


def query_api(prompt):
    """Query the Hugging Face API with a prompt."""
    try:
        if not api_key:
            return "Error: HUGGINGFACE_API_KEY is not set."
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
                "Hugging Face Inference Providers. Create or update the token with "
                "inference permissions, then run the script again."
            )
        if "404" in str(error):
            return (
                "Error: The selected Hugging Face model is not available for your "
                "current inference route. Try a different supported model."
            )
        return f"Error: {error!r}"
    except Exception as error:
        return f"Error: {error!r}"


# Main Execution
if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    user_prompt = input("Enter your prompt: ")
    print("Querying API...")
    result = query_api(user_prompt)
    print("Response:")
    print(result)
