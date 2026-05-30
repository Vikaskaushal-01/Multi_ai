from app.models.base_model import BaseModel


class LlamaModel(BaseModel):

    def __init__(self):

        super().__init__(
            "meta-llama/llama-3.1-8b-instruct"
        )