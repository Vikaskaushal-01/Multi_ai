from app.models.qwen_model import QwenModel
from app.models.llama_model import LlamaModel
from app.models.mistral_model import MistralModel
from app.models.deepseek_model import DeepSeekModel

from app.evaluator import get_best_response
from app.memory import get_history

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


def process_query(query, session_id):

    history = get_history(session_id)

    responses = []

    for model_name, model in models:

        try:

            response = model.generate(
                query,
                history
            )

            responses.append({
                "model": model_name,
                "response": response
            })

        except Exception as e:

            responses.append({
                "model": model_name,
                "response": f"Error: {str(e)}"
            })

    valid = []

    for item in responses:

        if "Error" not in item["response"]:
            valid.append(item)

    best, scored = get_best_response(
        query,
        valid
    )

    return {
        "best_model": best["model"],
        "best_response": best["response"],
        "scores": scored
    }