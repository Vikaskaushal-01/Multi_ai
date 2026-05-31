from app.models.base_model import (
    BaseModel
)


class MistralModel(

    BaseModel

):

    def __init__(self):

        super().__init__(

            "mistralai/mistral-7b-instruct"

        )