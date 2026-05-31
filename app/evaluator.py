from app.similarity import (
    calculate_similarity
)


def score_response(
    prompt,
    response
):

    similarity = calculate_similarity(
        prompt,
        [response]
    )[0]

    word_count = len(
        response.split()
    )

    length_score = min(
        word_count / 100,
        1
    )

    score = (
        similarity * 70
        +
        length_score * 30
    )

    return round(
        score,
        2
    )


def evaluate_models(
    prompt,
    model_outputs
):

    results = []

    for item in model_outputs:

        score = score_response(

            prompt,

            item["response"]

        )

        results.append({

            "model":
            item["model"],

            "response":
            item["response"],

            "score":
            score

        })

    best = max(

        results,

        key=lambda x:
        x["score"]

    )

    total = sum(

        item["score"]

        for item in results

    )

    graph_data = []

    for item in results:

        percentage = round(

            (
                item["score"]
                /
                total
            ) * 100,

            2

        )

        graph_data.append({

            "model":
            item["model"],

            "percentage":
            percentage,

            "score":
            item["score"]

        })

    return {

        "best_model":
        best["model"],

        "best_response":
        best["response"],

        "confidence":
        round(

            (
                best["score"]
                /
                total
            ) * 100,

            2

        ),

        "graph":
        graph_data

    }