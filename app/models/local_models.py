from transformers import pipeline

class LocalModels:

    def __init__(self):

        self.models = {

            "DeepSeek-Coder": pipeline(
                "text-generation",
                model="deepseek-ai/deepseek-coder-1.3b-base"
            ),

            "Qwen2.5": pipeline(
                "text-generation",
                model="Qwen/Qwen2.5-1.5B-Instruct"
            ),

            "Phi-2": pipeline(
                "text-generation",
                model="microsoft/phi-2"
            ),

            "TinyLlama": pipeline(
                "text-generation",
                model="TinyLlama/TinyLlama-1.1B-Chat-v1.0"
            ),

            "Flan-T5": pipeline(
                "text2text-generation",
                model="google/flan-t5-large"
            )
        }

    def generate(self, prompt):

        responses = []

        for model_name, model in self.models.items():

            try:

                result = model(
                    prompt,
                    max_new_tokens=256,
                    truncation=True
                )

                if isinstance(result, list):

                    if "generated_text" in result[0]:

                        text = result[0]["generated_text"]

                    else:

                        text = str(result)

                else:

                    text = str(result)

                responses.append({
                    "model": model_name,
                    "response": text
                })

            except Exception as e:

                responses.append({
                    "model": model_name,
                    "response": f"Error: {str(e)}"
                })

        return responses