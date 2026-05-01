def route_query(query: str) -> str:
    q = query.lower()

    if "solve" in q or "equation" in q or "math" in q:
        return "math"
    elif "code" in q or "python" in q or "bug" in q:
        return "code"
    else:
        return "theory"