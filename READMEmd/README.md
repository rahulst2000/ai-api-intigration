# # Generative AI API Integration (Python)

## Project Description

This project demonstrates how to integrate multiple Generative AI APIs using Python.
Each Python program connects to a different AI provider, sends a user prompt, and prints the generated response in the terminal.

The project covers the following AI services:

* OpenAI
* Groq
* Ollama
* Hugging Face
* Google Gemini
* Cohere
* multi_api_query 

## Project Structure

ai-api-integration/
├── openai_example.py
├── groq_example.py
├── ollama_example.py
├── huggingface_example.py
├── gemini_example.py
├── cohere_example.py
├── multi_api_query.py
├── requirements.txt
├── README.md

└── screenshots/
  ├── openai_output.png
  ├── groq_output.png
  ├── ollama_output.png
  ├── huggingface_output.png
  ├── gemini_output.png
  └── cohere_output.png

---

## Requirements

* Python 3.8 or higher
* Internet connection
* API keys for each provider

Install dependencies using:

pip install -r requirements.txt

## How to Obtain API Keys

### Groq

1. Go to https://console.groq.com
2. Sign up and create an API key

### Google Gemini

1. Visit https://aistudio.google.com
2. Generate an API key

### Hugging Face

1. Visit https://huggingface.co
2. Open **Settings → Access Tokens**
3. Generate a new token

### Cohere

1. Visit https://dashboard.cohere.com
2. Create an API key

### Ollama

1. Download from https://ollama.com
2. Install and run a model locally

Example command:

ollama run llama3

---

## How to Run Each Program

Example command:

python groq_example.py

After running, the program will ask for input:

Enter your prompt:

Example prompt:

Explain Artificial Intelligence in simple terms.

The AI-generated response will be printed in the terminal.

---

## Screenshots

The **screenshots** folder contains output screenshots from each API program execution.

Files included:

* openai_output.png
* groq_output.png
* ollama_output.png
* huggingface_output.png
* gemini_output.png
* cohere_output.png

Each screenshot shows the prompt entered and the AI-generated response.
### Note
### Ollama Note

Ollama runs large language models locally on your system.
Unlike other APIs that run in the cloud, Ollama downloads the model to your computer.
Because of this, additional system storage is required.
Example:

Running the following command downloads the Llama3 model locally:
ollama run llama3
The model size may require **3GB–8GB of disk space**, depending on the model version.
Minimum recommended system requirements:
* 8 GB RAM
* 10 GB free disk space
* Internet connection for initial model download
After the model is downloaded, prompts can be executed locally without external API calls.
