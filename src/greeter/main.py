"""Main greeting function"""


def greet(name: str) -> str:
    """Return a friendly greeting for the given name."""
    return f"Hello, {name}! Hei!"


def main():
    name = input("What is your name? ").strip() or "friend"
    print(greet(name))
