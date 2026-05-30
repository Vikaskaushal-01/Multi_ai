from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.router import process_query
from app.memory import save_message
from app.memory import get_history

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):

    session_id: str
    query: str


@app.post("/chat")
def chat(request: ChatRequest):

    save_message(
        request.session_id,
        "user",
        request.query
    )

    result = process_query(
        request.query,
        request.session_id
    )

    save_message(
        request.session_id,
        "assistant",
        result["best_response"]
    )

    return {
        "response": result["best_response"],
        "best_model": result["best_model"],
        "scores": result["scores"],
        "history": get_history(
            request.session_id
        )
    }