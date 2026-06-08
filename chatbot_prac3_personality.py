# System prompt (give your bot a personality)
# What changed — just one thing:
# The history list now starts with a system message instead of being empty. 
# The "system" role is special — it's instructions to the model, not part of the conversation. The model treats it as its identity and rules.

# System prompts are how you customise LLM behaviour without retraining the model. 
# They sit at the top of the context window and act as persistent instructions throughout the conversation."

import ollama

history = [
    {
        "role": "system",
        "content": "You are a funny pirate. You speak like a pirate and use sea refeences everywhere"
    }
]

def chat(user_message):
    history.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    response = ollama.chat(
        model= "llama3.2",

        messages=history
    )

    assistant_response = response['message']['content']

    history.append(
        {
            "role": "assistant",
            "content": assistant_response
        }
    )

    return assistant_response


print(chat("Explain Neural Networks"))

# Same model. Same question. Completely different output.
# The only thing that changed was the system prompt. The model didn't retrain, didn't update, didn't change at all. You just instructed it differently.
# This is how every AI product is built:

# ChatGPT — system prompt telling it to be a helpful assistant
# GitHub Copilot — system prompt telling it to be a coding assistant
# Customer support bots — system prompt with company knowledge and tone rules
# Your future projects — whatever you want