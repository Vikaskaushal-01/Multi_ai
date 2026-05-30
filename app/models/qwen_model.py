from app.models.base_model import BaseModel


class QwenModel(BaseModel):

    def __init__(self):

        super().__init__(
            "qwen/qwen-2.5-7b-instruct"
        )