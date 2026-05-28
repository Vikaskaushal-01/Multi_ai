ENGINEERING_KEYWORDS = [
    "python",
    "java",
    "javascript",
    "react",
    "node",
    "docker",
    "sql",
    "mongodb",
    "api",
    "machine learning",
    "deep learning",
    "math",
    "ai",
    "engineering",
    "algorithm",
    "data structure",
    "cloud",
    "backend",
    "frontend"
]

def is_engineering_query(query: str):

    query = query.lower()

    return any(
        keyword in query
        for keyword in ENGINEERING_KEYWORDS
    )