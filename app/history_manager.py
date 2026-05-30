import json
import os
import uuid

DATA_FILE = "data/chats.json"


def _ensure_file():

    os.makedirs("data", exist_ok=True)

    if not os.path.exists(DATA_FILE):

        with open(DATA_FILE, "w") as f:

            json.dump(
                {"chats": []},
                f,
                indent=4
            )


def load_chats():

    _ensure_file()

    with open(DATA_FILE, "r") as f:

        return json.load(f)


def save_chats(data):

    with open(DATA_FILE, "w") as f:

        json.dump(
            data,
            f,
            indent=4
        )


def create_chat(title):

    data = load_chats()

    chat_id = str(uuid.uuid4())

    data["chats"].append({

        "id": chat_id,
        "title": title,
        "messages": []

    })

    save_chats(data)

    return chat_id


def get_chat(chat_id):

    data = load_chats()

    for chat in data["chats"]:

        if chat["id"] == chat_id:

            return chat

    return None


def save_message(chat_id, role, content):

    data = load_chats()

    for chat in data["chats"]:

        if chat["id"] == chat_id:

            chat["messages"].append({

                "role": role,
                "content": content

            })

            break

    save_chats(data)


def get_history(chat_id):

    chat = get_chat(chat_id)

    if not chat:

        return []

    return chat["messages"]


def get_all_chats():

    return load_chats()["chats"]