from app.similarity import (
    calculate_similarity
)


def score_response(

    prompt,
    response

):

    score = 0

    response_lower = response.lower()

    # Similarity

    similarity = calculate_similarity(

        prompt,
        [response]

    )[0]

    score += similarity * 60

    # Length Quality

    words = len(response.split())

    if words > 50:
        score += 20

    elif words > 25:
        score += 10

    # Technical Quality

    technical_keywords = [

        "algorithm",
        "function",
        "class",
        "example",
        "python",
        "database",
        "api",
        "model",
        "machine learning"

    ]

    for keyword in technical_keywords:

        if keyword in response_lower:

            score += 2

    # Penalties

    bad_words = [

        "error",
        "failed",
        "cannot",
        "unavailable"

    ]

    for word in bad_words:

        if word in response_lower:

            score -= 10

    return round(score, 2)


def evaluate_models(

    prompt,
    model_outputs

):

    results = []

    for item in model_outputs:

        model_name = item["model"]

        response = item["response"]

        score = score_response(

            prompt,
            response

        )

        results.append({

            "model": model_name,

            "response": response,

            "score": score

        })

    best = max(

        results,

        key=lambda x: x["score"]

    )

    total = sum(

        item["score"]

        for item in results

    )

    graph_data = []

    for item in results:

        percentage = round(

            (
                item["score"] /
                total
            ) * 100,

            2

        )

        graph_data.append({

            "model":
            item["model"],

            "percentage":
            percentage

        })

    return {

        "best_model":
        best["model"],

        "best_response":
        best["response"],

        "confidence":
        round(

            (
                best["score"] /
                total
            ) * 100,

            2

        ),

        "graph":
        graph_data

    }