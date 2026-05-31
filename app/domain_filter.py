ENGINEERING_KEYWORDS = [

    "python",
    "java",
    "c++",
    "javascript",
    "react",
    "node",
    "sql",
    "mongodb",
    "docker",
    "kubernetes",

    "ai",
    "artificial intelligence",
    "machine learning",
    "deep learning",

    "data structure",
    "algorithm",

    "backend",
    "frontend",
    "api",
    "database",

    "cloud",
    "devops",

    "math",
    "mathematics",
    "engineering",

    "computer science"
]


def is_engineering_query(query):

    query = query.lower()

    return any(

        keyword in query

        for keyword in ENGINEERING_KEYWORDS
    )