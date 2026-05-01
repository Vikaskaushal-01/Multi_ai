def is_engineering_query(query: str) -> bool:
    keywords = [
        "code", "algorithm", "math", "data", "machine learning",
        "engineering", "python", "react", "api", "database"
    ]
    return any(k in query.lower() for k in keywords)