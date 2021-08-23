def hello(name: str) -> str:
    """Returns default hello message for the project"""
    if name is None:
        raise ValueError("Name must be defined")
    if not name.strip():
        raise ValueError("Name must be non-empty")
    return f'Hello project "{name}"'
