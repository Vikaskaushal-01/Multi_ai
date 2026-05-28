class BaseModel:

    async def generate(self, prompt: str):
        raise NotImplementedError