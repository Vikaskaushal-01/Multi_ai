ENGINEERING_KEYWORDS = [
    "python",
    "java",
    "c++",
    "javascript",
    "react",
    "backend",
    "frontend",
    "database",
    "ai",
    "machine learning",
    "deep learning",
    "math",
    "calculus",
    "linear algebra",
    "algorithm",
    "data structure",
    "computer science",
    "engineering",
    "cloud",
    "docker",
    "api",
    "sql",
    "mongodb",
    "networking"
]


def is_engineering_query(query: str) -> bool:
    query = query.lower()
    return any(keyword in query for keyword in ENGINEERING_KEYWORDS)