from app.models.qwen_model import QwenModel
from app.models.llama_model import LlamaModel
from app.models.mistral_model import MistralModel
from app.models.deepseek_model import DeepSeekModel

from app.evaluator import get_best_response

qwen = QwenModel()
llama = LlamaModel()
mistral = MistralModel()
deepseek = DeepSeekModel()

models = [

    ("Qwen", qwen),
    ("Llama", llama),
    ("Mistral", mistral),
    ("DeepSeek", deepseek)
]


def process_query(query):

    responses = []

    for model_name, model in models:

        try:

            response = model.generate(query)

            responses.append({

                "model": model_name,
                "response": response
            })

        except Exception as e:

            responses.append({

                "model": model_name,
                "response": f"Error: {str(e)}"
            })

    valid_responses = []

    for response in responses:

        if "Error" not in response["response"]:

            valid_responses.append(response)

    if not valid_responses:

        return (
            "All AI models failed. "
            "Check OpenRouter API key."
        )

    best = get_best_response(valid_responses)

    return (
        f"Best Model: {best['model']}\n\n"
        f"{best['response']}"
    )