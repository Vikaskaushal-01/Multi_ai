def score_response(response: str) -> float:
    score = 0

    if len(response) > 50:
        score += 1
    if "error" not in response.lower():
        score += 1
    if "." in response:
        score += 1

    return score


def select_best(responses):
    best = max(responses, key=lambda x: x["score"])
    return best["response"]