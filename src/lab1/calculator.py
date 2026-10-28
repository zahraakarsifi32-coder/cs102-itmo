"""Simple calculator."""


def add(first: float, second: float) -> float:
    """Return the sum of two numbers."""
    return first + second


def subtract(first: float, second: float) -> float:
    """Return the difference of two numbers."""
    return first - second


def multiply(first: float, second: float) -> float:
    """Return the product of two numbers."""
    return first * second


def divide(first: float, second: float) -> float:
    """Return the quotient of two numbers."""
    if second == 0:
        raise ValueError("Cannot divide by zero")
    return first / second
