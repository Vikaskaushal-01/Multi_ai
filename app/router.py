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

from app.evaluator import (
    evaluate_models
)

qwen = QwenModel()

llama = LlamaModel()

mistral = MistralModel()

deepseek = DeepSeekModel()


MODELS = [

    (
        "Qwen",
        qwen
    ),

    (
        "Llama",
        llama
    ),

    (
        "Mistral",
        mistral
    ),

    (
        "DeepSeek",
        deepseek
    )
]


def process_query(

    prompt,
    history

):

    model_outputs = []

    for name, model in MODELS:

        try:

            response = model.generate(

                prompt,
                history

            )

            model_outputs.append({

                "model": name,

                "response": response

            })

        except Exception as e:

            print(
                f"{name}:",
                e
            )

    if not model_outputs:

        raise Exception(
            "All models failed."
        )

    return evaluate_models(

        prompt,
        model_outputs

    )