# Creating a simple Chatbot here using ollama (self hosted open sourced models - llama3.2 here)
# What changed — just 2 things:
# history list starts empty, and we append every message to it — both yours and the model's reply
# We pass the entire history to every ollama.chat() call instead of just one message

import ollama

history = []

def chat(user_message):

    history.append({
        "role": "user",
        "content": user_message
    })

    response = ollama.chat(
        model = "llama3.2",

        messages = history
    )

    assistant_message = response['message']['content']

    history.append({
        "role": "assistant",
        "content": assistant_message
    })

    return assistant_message


print(chat("Hi! My name is Nishita"))
print(chat("What's my name?"))

print("\n--- History ---")
for msg in history:
    print(msg['role'], ":", msg['content'])