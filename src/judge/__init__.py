from __future__ import annotations

def add(a, b):
    """Возвращает сумму a и b."""
    return a + b

def subtract(a, b):
    """Возвращает разность a - b."""
    return a - b

def multiply(a, b):
    """Возвращает произведение a * b."""
    return a * b

def divide(a, b):
    """Возвращает частное a / b. При делении на ноль выбрасывает ZeroDivisionError."""
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b

__all__ = ["add", "subtract", "multiply", "divide"]
