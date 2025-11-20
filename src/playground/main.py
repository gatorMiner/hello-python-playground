def hello(name: str = "World") -> str:
    """Return a Hello message for name.

    Args:
        name: name to include in the greeting.

    Returns:
        Greeting string.
    """
    if not name:
        name = "World"
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(hello())
