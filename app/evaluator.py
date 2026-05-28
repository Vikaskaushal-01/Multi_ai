def score_response(response: str):

    score = 0

    if len(response) > 50:
        score += 2

    if "error" not in response.lower():
        score += 2

    if len(response.split()) > 25:
        score += 2

    if "example" in response.lower():
        score += 2

    return score

def get_best_response(responses):

    scored = []

    for response in responses:

        score = score_response(response)

        scored.append((response, score))

    best = max(
        scored,
        key=lambda x: x[1]
    )

    return best[0]