from __future__ import annotations

def add(a, b):
    """
    Возвращает сумму a и b.
    Допускает int/float/Decimal и их миксы.
    """
    return a + b

__all__ = ["add"]
