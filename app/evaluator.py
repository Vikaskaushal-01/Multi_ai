from app.similarity import calculate_similarity


def get_best_response(prompt, responses):

    response_texts = [
        item["response"]
        for item in responses
    ]

    similarities = calculate_similarity(
        prompt,
        response_texts
    )

    scored = []

    for i, item in enumerate(responses):

        similarity_score = similarities[i]

        length_score = min(
            len(item["response"]) / 200,
            1
        )

        total_score = (
            similarity_score * 0.7 +
            length_score * 0.3
        )

        scored.append({
            "model": item["model"],
            "response": item["response"],
            "score": round(total_score, 3)
        })

    best = max(
        scored,
        key=lambda x: x["score"]
    )

    return best, scored