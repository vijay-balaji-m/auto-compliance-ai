import ollama
from app.rag import get_context
from app.prompts import system_prompt

model = 'phi3'

def build_prompt(context):
    return system_prompt.replace("<<context>>", context)

def chat(messages):
    response = ollama.chat(
        model=model,
        messages=messages
    )

    content = response['message']['content']
    chat_history.append({
        "role": "assistant",
        "content": content
    })

    print(f"Bot: {content}\n")

if __name__ == "__main__":
    chat_history = []

    while True:
        user_input = input("You: ")
        context, sources = get_context(user_input)
        system_prompt = build_prompt(context)
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ]

        chat_history.extend(messages)
        if user_input == 'exit':
            break

        chat(messages)