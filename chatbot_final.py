# Two new things here:
# 1. Streaming — stream=True makes the response print word by word as it generates, instead of waiting for the full response. That's exactly how ChatGPT's typing effect works.
# 2. The while True loop — keeps the chat alive until you type bye. Every iteration appends to history, so memory is maintained throughout.


import ollama

history = [
    {
        "role": "system",
        "content": "You are a helpful AI tutor named Aria. You teach complex tech concepts in simple terms. You always use short, clear explanations and real world analogies. You never use jargon without explaining it first."
    }
]

def chat(user_message):
    history.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    stream = ollama.chat(
        model = "llama3.2",
        messages=history,
        stream=True
    )

    assistant_message = ""
    for chunk in stream:
        piece = chunk['message']['content']
        print(piece, end=" ", flush=True)
        assistant_message+=piece
    
    print()

    history.append(
        {
            "role": "assistant",
            "content": assistant_message
        }
    )


print("Aria is ready! Type 'bye' to exit.\n")


# Live Chat
while True:
    user_input = input("You: ")

    if user_input.lower() == "bye":
        print("Aria: Goodbye! Happy learning!")
        break

    print("Aria: ", end="")
    chat(user_input)
    print()


