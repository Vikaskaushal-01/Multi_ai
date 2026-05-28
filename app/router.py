import asyncio

from app.models.qwen_model import QwenModel
from app.models.llama_model import LlamaModel
from app.models.mistral_model import MistralModel
from app.models.deepseek_model import DeepSeekModel

from app.evaluator import get_best_response

qwen = QwenModel()
llama = LlamaModel()
mistral = MistralModel()
deepseek = DeepSeekModel()

async def safe_generate(model, query):

    try:

        return await asyncio.wait_for(
            model.generate(query),
            timeout=120
        )

    except Exception as e:

        return f"Error: {str(e)}"

async def process_query(query: str):

    tasks = [
        safe_generate(qwen, query),
        safe_generate(llama, query),
        safe_generate(mistral, query),
        safe_generate(deepseek, query)
    ]

    responses = await asyncio.gather(*tasks)

    valid_responses = [
        response for response in responses
        if "Error" not in response
    ]

    if not valid_responses:

        return "All models failed."

    return get_best_response(valid_responses)