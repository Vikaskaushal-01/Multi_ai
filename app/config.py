import os
from dotenv import load_dotenv

load_dotenv()

HF_API_KEY = os.getenv("HUGGINGFACE_API_KEY")

MODEL_ENDPOINTS = {
    "math": "google/flan-t5-large",
    "code": "bigcode/starcoder",
    "theory": "meta-llama/Llama-2-7b-chat-hf"
}