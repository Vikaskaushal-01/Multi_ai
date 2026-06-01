import json
import uuid
import os

DATA_FILE = "data/chats.json"


def ensure_file():

    os.makedirs(
        "data",
        exist_ok=True
    )

    if not os.path.exists(DATA_FILE):

        with open(
            DATA_FILE,
            "w"
        ) as f:

            json.dump(
                {
                    "chats": []
                },
                f,
                indent=4
            )


def load_data():

    ensure_file()

    with open(
        DATA_FILE,
        "r"
    ) as f:

        return json.load(f)


def save_data(data):

    with open(
        DATA_FILE,
        "w"
    ) as f:

        json.dump(
            data,
            f,
            indent=4
        )


def create_chat():

    data = load_data()

    chat_id = str(
        uuid.uuid4()
    )

    chat = {

        "id": chat_id,

        "title": "New Chat",

        "messages": []

    }

    data["chats"].append(
        chat
    )

    save_data(data)

    return chat_id


def update_chat_title(

    chat_id,
    title

):

    data = load_data()

    for chat in data["chats"]:

        if chat["id"] == chat_id:

            if chat["title"] == "New Chat":

                chat["title"] = title[:50]

    save_data(data)


def save_message(
    chat_id,
    role,
    content
):

    data = load_data()

    for chat in data["chats"]:

        if chat["id"] == chat_id:

            chat["messages"].append({

                "role": role,

                "content": content

            })

            break

    save_data(data)


def get_history(chat_id):

    data = load_data()

    for chat in data["chats"]:

        if chat["id"] == chat_id:

            return chat["messages"]

    return []


def get_all_chats():

    data = load_data()

    return data["chats"]