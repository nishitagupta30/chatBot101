# Creating a simple Chatbot here using ollama (self hosted open sourced models - llama3.2 here)
# The issue with this is that the model does not have any context/converstaion history
# Hence after asking one question, and replacing it with other, both time separate results

# What's happening in these lines:
# ollama.chat() — sends a request to your locally running model
# model — which model to use
# messages — a list of messages. Each message has a role and content
# role can be "user" (you) or "assistant" (the model)
# The response comes back as a dict, and the actual text lives at response['message']['content']

import ollama

# response = ollama.chat(
#     model = 'llama3.2',
#     messages = [
#         {"role": 'user', "content": "Hi! My name is Nishita."}
#     ]
# )

#response : Hello Nishita! It's nice to meet you. Is there something I can help you with or would you like to chat?

response = ollama.chat(
    model = 'llama3.2',
    messages = [
        {"role": 'user', "content": "Hey! Do you know my name?"}
    ]
)
# I'm happy to chat with you, but I don't have any information about your identity or personal details. This is our first conversation, and I don't retain any data about individual users. Would you like to introduce yourself?
# Forgot everything here no context at all, need to create memory for it.

print(response)