# ChatBot AI Agent 🤖

A locally running AI chatbot with memory, built using Python and Ollama. No API key required, runs completely free on your machine.

## What it does

- Remembers your entire conversation (stateful memory)
- Streams responses word by word like ChatGPT
- Has a custom AI tutor persona (Aria)
- Runs 100% locally — no internet needed after setup

## How memory works

LLMs are stateless by default — they forget everything after each call. This chatbot maintains a `history` list and sends the full conversation with every request, so the model always has context.

## Setup

### 1. Install Ollama

Go to [ollama.com](https://ollama.com) and download for your OS (Mac / Windows / Linux). Install it like any normal app.

Verify it works:
```bash
ollama --version
```

### 2. Pull the model

```bash
ollama pull llama3.2
```

This downloads the model (~2GB). One time only.

### 3. Test Ollama is working

```bash
ollama run llama3.2
```

You should get a chat prompt in your terminal. Type `/bye` to exit.

### 4. Install Python dependency

```bash
pip install ollama
```

### 5. Run the chatbot

```bash
python chatbot.py
```

Type anything and chat with Aria. Type `bye` to exit.

## Requirements

- Python 3.8+
- 8GB RAM minimum
- Ollama installed
- llama3.2 model pulled

## Project structure

```
ChatBot_AI_Agent/
├── chatbot.py      # Main chatbot code
├── .gitignore      # Ignores pycache, .env files
└── README.md       # This file
```

## Concepts covered

| Concept | Description |
|---|---|
| Stateless LLM | Models don't remember between calls by default |
| Conversation history | Array of messages sent with every API call |
| Context window | How much text the model can read at once |
| System prompt | Instructions that define the model's behaviour |
| Streaming | Word by word response delivery |

## Built with

- [Ollama](https://ollama.com) — run LLMs locally
- [Llama 3.2](https://ollama.com/library/llama3.2) — open source model by Meta
- Python 3

---

*Project 1 of AI learning series — next up: RAG (Retrieval Augmented Generation)*
