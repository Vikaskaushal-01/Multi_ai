import aiohttp

from app.config import HUGGINGFACE_API_KEY

class DeepSeekModel:

    def __init__(self):

        self.url = (
            "https://api-inference.huggingface.co/models/"
            "deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"
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

                return "DeepSeek failed"