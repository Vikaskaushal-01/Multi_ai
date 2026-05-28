from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.router import process_query

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

    response = process_query(
        request.query
    )

    return {
        "response": response
    }