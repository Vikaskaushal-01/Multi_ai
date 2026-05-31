from fastapi import FastAPI
from app.history_manager import update_chat_title
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel

from app.router import process_query

from app.history_manager import (
    create_chat,
    save_message,
    get_history,
    get_all_chats
)



from app.domain_filter import (
    is_engineering_query
)

app = FastAPI()

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]

)


class ChatRequest(BaseModel):

    chat_id: str
    query: str


@app.get("/chats")

def chats():

    return get_all_chats()


@app.post("/new-chat")

def new_chat():

    chat_id = create_chat(
        "New Chat"
    )

    return {

        "chat_id":
        chat_id

    }


@app.post("/chat")

def chat(req: ChatRequest):

    if not is_engineering_query(
        req.query
    ):

        return {

            "response":
            "Sorry, I only answer engineering and technical questions."

        }

    history = get_history(
        req.chat_id
    )

    save_message(

        req.chat_id,

        "user",

        req.query

    )

    result = process_query(

        req.query,

        history

    )

    save_message(

        req.chat_id,

        "assistant",

        result["response"]

    )

    return result