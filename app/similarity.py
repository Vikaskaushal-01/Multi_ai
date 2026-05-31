from sklearn.feature_extraction.text import (
    TfidfVectorizer
)

from sklearn.metrics.pairwise import (
    cosine_similarity
)


def calculate_similarity(

    prompt,
    responses

):

    texts = [prompt] + responses

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(texts)

    similarities = cosine_similarity(

        vectors[0:1],
        vectors[1:]

    )

    return similarities[0]