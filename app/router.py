from app.models.qwen_model import (
    QwenModel
)

from app.models.llama_model import (
    LlamaModel
)

from app.models.mistral_model import (
    MistralModel
)

from app.models.deepseek_model import (
    DeepSeekModel
)

from app.evaluator import evaluate


qwen = QwenModel()
llama = LlamaModel()
mistral = MistralModel()
deepseek = DeepSeekModel()


MODELS = [

    ("Qwen", qwen),
    ("Llama", llama),
    ("Mistral", mistral),
    ("DeepSeek", deepseek)

]


def process_query(

    prompt,
    history

):

    results = []

    for name, model in MODELS:

        try:

            answer = model.generate(
                prompt,
                history
            )

            results.append({

                "model":
                name,

                "response":
                answer

            })

        except Exception as e:

            print(
                f"{name} error:",
                e
            )

    if not results:

        raise Exception(
            "All models failed."
        )

    best, scores = evaluate(
        prompt,
        results
    )

    return {

        "best_model":
        best["model"],

        "response":
        best["response"],

        "scores":
        scores

    }