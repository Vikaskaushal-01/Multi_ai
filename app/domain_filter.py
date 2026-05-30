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
    "artificial intelligence",
    "ai",
    "data structure",
    "algorithm",
    "backend",
    "frontend",
    "cloud",
    "devops",
    "engineering",
    "math",
    "mathematics",
    "computer science"
]

def is_engineering_query(query: str) -> bool:
    query = query.lower()

    return any(
        keyword in query
        for keyword in ENGINEERING_KEYWORDS
    )