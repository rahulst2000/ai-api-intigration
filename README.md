# Generative AI API Integration

This project contains simple Python examples for calling multiple AI providers from the terminal.

Included providers:

- Groq
- Google Gemini
- Cohere
- Hugging Face
- Ollama
- Multi-provider query example

## Project Files

- `groq_example.py`
- `gemini_example.py`
- `cohere_example.py`
- `huggingface_example.py`
- `ollama_example.py`
- `multi_api_query.py`
- `.env.example`
- `requirements.txt`

## Requirements

- Python 3.10 or higher recommended
- Internet access for Groq, Gemini, Cohere, and Hugging Face
- Ollama installed locally for `ollama_example.py`

## Install Dependencies

Create and activate a virtual environment if you want an isolated setup:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

## Environment Setup

Create a local `.env` file from `.env.example` and add your real API keys:

```env
GROQ_API_KEY=your_groq_api_key
COHERE_API_KEY=your_cohere_api_key
HUGGINGFACE_API_KEY=your_huggingface_api_key
GEMINI_API_KEY=your_gemini_api_key
OLLAMA_HOST=http://localhost:11434
OLLAMA_API_KEY=your_ollama_api_key
```

`.env` is ignored by git and will not be pushed.

## How To Run

Run any script with Python:

```powershell
python groq_example.py
python gemini_example.py
python cohere_example.py
python huggingface_example.py
python ollama_example.py
python multi_api_query.py
```

Each script will prompt you with:

```text
Enter your prompt:
```

## Ollama Setup

Install Ollama from `https://ollama.com`, then pull a local model:

```powershell
ollama run llama3
```

Note:

- Ollama runs locally on your machine
- The selected model may need several GB of RAM
- The first run may download model files before it can answer prompts

## Screenshots

Reference screenshots are stored in the `READMEmd/` folder.

