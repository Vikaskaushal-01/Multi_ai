from fastapi import FastAPI
from pydantic import BaseModel

from app.classifier import is_engineering_query
from app.router import route_query
from app.model_handler import query_model
from app.evaluator import score_response, select_best
from app.memory import MemoryStore
from app.self_optimizer import SelfOptimizer

app = FastAPI()

memory = MemoryStore()
optimizer = SelfOptimizer()


class ChatRequest(BaseModel):
    session_id: str
    query: str


@app.get("/")
def home():
    return {"message": "Multi-Model AI Backend is running 🚀"}


@app.post("/chat")
def chat(request: ChatRequest):

    query = request.query
    session_id = request.session_id

    # 1. Engineering filter
    if not is_engineering_query(query):
        return {
            "response": "❌ Sorry, this chatbot is only for engineering-related topics."
        }

    category = route_query(query)

    responses = []

    for model_type in ["math", "code", "theory"]:
        res = query_model(model_type, query)
        score = score_response(res)

        responses.append({
            "response": res,
            "score": score,
            "model": model_type
        })

    best_response = select_best(responses)

    memory.add(session_id, query, best_response)

    avg_score = sum([r["score"] for r in responses]) / len(responses)
    optimizer.adjust(avg_score)

    return {
        "response": best_response,
        "category": category,
        "temperature": optimizer.temperature
    }