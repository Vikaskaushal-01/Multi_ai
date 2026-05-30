import requests
import os

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv(
    "OPENROUTER_API_KEY"
)


class BaseModel:

    def __init__(self, model_name):

        self.model_name = model_name

    def generate(self, prompt, history=None):

        messages = []

        if history:

            for item in history[-6:]:

                messages.append({
                    "role": item["role"],
                    "content": item["message"]
                })

        messages.append({
            "role": "user",
            "content": prompt
        })

        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": self.model_name,
                "messages": messages
            }
        )

        data = response.json()

        if "choices" not in data:
            return f"API Error: {data}"

        return data[
            "choices"
        ][0]["message"]["content"]