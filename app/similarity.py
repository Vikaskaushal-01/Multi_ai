from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(
    prompt,
    responses
):

    texts = [prompt] + responses

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(texts)

    scores = cosine_similarity(
        vectors[0:1],
        vectors[1:]
    )

    return [
        float(x)
        for x in scores[0]
    ]