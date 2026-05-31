from fastapi import FastAPI

from fastapi.middleware.cors import (
    CORSMiddleware
)

from pydantic import BaseModel

from app.router import (
    process_query
)

from app.domain_filter import (
    is_engineering_query
)

from app.history_manager import (

    create_chat,

    update_chat_title,

    save_message,

    get_history,

    get_all_chats

)

app = FastAPI()

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)


class ChatRequest(

    BaseModel

):

    chat_id: str

    query: str


@app.get("/chats")

def chats():

    return get_all_chats()


@app.post("/new-chat")

def new_chat():

    chat_id = create_chat()

    return {

        "chat_id":
        chat_id

    }


@app.post("/chat")

def chat(

    request:
    ChatRequest

):

    if not is_engineering_query(

        request.query

    ):

        return {

            "response":
            "Sorry, I only answer engineering and technical questions."

        }

    history = get_history(

        request.chat_id

    )

    update_chat_title(

        request.chat_id,

        request.query

    )

    save_message(

        request.chat_id,

        "user",

        request.query

    )

    result = process_query(

        request.query,

        history

    )

    save_message(

    request.chat_id,

    "assistant",

    {

        "response":
        result["best_response"],

        "best_model":
        result["best_model"],

        "confidence":
        result["confidence"],

        "graph":
        result["graph"]

    }

)

    return {

        "best_model":
        result["best_model"],

        "confidence":
        result["confidence"],

        "response":
        result["best_response"],

        "graph":
        result["graph"]

    }