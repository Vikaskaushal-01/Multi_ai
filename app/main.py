from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.router import process_query
from app.domain_filter import is_engineering_query
from app.memory import save_message, get_history

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


@app.get("/")
def home():
    return {
        "message": "Multi-Model AI Optimizer Running"
    }


@app.post("/chat")
async def chat(request: ChatRequest):
    query = request.query
    session_id = request.session_id

    if not is_engineering_query(query):
        return {
            "response": "Sorry, this chatbot is only designed for engineering-related topics."
        }

    save_message(session_id, "user", query)

    response = await process_query(query)

    save_message(session_id, "assistant", response)

    return {
        "response": response,
        "history": get_history(session_id)
    }