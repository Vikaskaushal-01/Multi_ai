def score_response(response):

    score = 0

    response = response.lower()

    if len(response) > 100:
        score += 3

    keywords = [

        "python",
        "example",
        "function",
        "class",
        "algorithm",
        "code"
    ]

    for keyword in keywords:

        if keyword in response:
            score += 1

    bad_words = [
        "error",
        "failed"
    ]

    for word in bad_words:

        if word in response:
            score -= 5

    return score


def get_best_response(responses):

    scored = []

    for item in responses:

        score = score_response(
            item["response"]
        )

        scored.append({

            "model": item["model"],
            "response": item["response"],
            "score": score
        })

    best = max(
        scored,
        key=lambda x: x["score"]
    )

    return best