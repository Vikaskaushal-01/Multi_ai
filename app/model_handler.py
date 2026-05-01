import requests
from app.config import HF_API_KEY, MODEL_ENDPOINTS

def query_model(model_type, prompt):
    model = MODEL_ENDPOINTS[model_type]

    url = f"https://api-inference.huggingface.co/models/{model}"

    headers = {
        "Authorization": f"Bearer {HF_API_KEY}"
    }

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_length": 200,
            "temperature": 0.7
        }
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=20)
        data = response.json()

        if isinstance(data, list):
            return data[0].get("generated_text", "No response")
        elif isinstance(data, dict) and "error" in data:
            return f"Model Error: {data['error']}"
        else:
            return str(data)

    except Exception as e:
        return f"Request failed: {str(e)}"