# app/operations/__init__.py

"""
Core mathematical operations for the calculator application.
"""

from typing import Union

Number = Union[int, float]

def add(a: Number, b: Number) -> Number:
    """Adds two numbers."""
    return a + b

def subtract(a: Number, b: Number) -> Number:
    """Subtracts the second number from the first."""
    return a - b

def multiply(a: Number, b: Number) -> Number:
    """Multiplies two numbers."""
    return a * b

def divide(a: Number, b: Number) -> float:
    """Divides the first number by the second. Raises ValueError if dividing by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return float(a / b)

def modulo(a: Number, b: Number) -> Number:
    """
    Performs the modulo operation (remainder of division).
    Raises ValueError if modulo by zero.
    """
    if b == 0:
        raise ValueError("Cannot perform modulo by zero!")
    return a % b

