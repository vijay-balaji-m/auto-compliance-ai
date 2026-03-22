from fastapi import FastAPI
from pydantic import BaseModel
import ollama

from app.rag import get_context
from app.prompts import system_prompt

app = FastAPI()

class Query(BaseModel):
    question: str

def build_prompt(context):
    return system_prompt.replace("<<context>>", context)

@app.post("/chat")
def chat(query: Query):
    context = get_context(query.question)
    prompt = build_prompt(context)

    response = ollama.chat(
        model="phi3",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": query.question}
        ]
    )

    return {
        "response": response["message"]["content"]
    }