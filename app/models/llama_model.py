import aiohttp

from app.config import HUGGINGFACE_API_KEY

class LlamaModel:

    def __init__(self):

        self.url = (
            "https://api-inference.huggingface.co/models/"
            "meta-llama/Llama-3.1-8B-Instruct"
        )

    async def generate(self, prompt: str):

        headers = {
            "Authorization":
            f"Bearer {HUGGINGFACE_API_KEY}"
        }

        payload = {
            "inputs": prompt
        }

        async with aiohttp.ClientSession() as session:

            async with session.post(
                self.url,
                headers=headers,
                json=payload
            ) as response:

                data = await response.json()

                if isinstance(data, list):

                    return data[0].get(
                        "generated_text",
                        "No response"
                    )

                return "Llama failed"