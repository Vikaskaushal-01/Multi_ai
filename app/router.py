import asyncio
from app.models.openai_model import OpenAIModel
from app.models.hf_model import HFModel
from app.evaluator import get_best_response


openai_model = OpenAIModel()
hf_model = HFModel()


async def process_query(query: str):
    tasks = [
        openai_model.generate(query),
        hf_model.generate(query)
    ]

    responses = await asyncio.gather(*tasks)

    best_response = get_best_response(responses)

    return best_response