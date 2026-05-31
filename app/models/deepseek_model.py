from app.models.base_model import (
    BaseModel
)


class DeepSeekModel(

    BaseModel

):

    def __init__(self):

        super().__init__(

            "deepseek/deepseek-r1"

        )