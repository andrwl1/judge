import math
import decimal
import pytest
from judge import add, subtract, multiply

# --- add ---
@pytest.mark.parametrize("a,b,expected", [
    (0, 0, 0),
    (2, 3, 5),
    (-4, 9, 5),
    (1.5, 2.5, 4.0),
    (10**12, 10**12, 2*10**12),
])
def test_add_basic(a, b, expected):
    assert add(a, b) == expected

def test_add_decimal():
    d1 = decimal.Decimal("1.10")
    d2 = decimal.Decimal("2.30")
    assert add(d1, d2) == decimal.Decimal("3.40")

def test_add_commutative():
    for a, b in [(7, -3), (0.1, 0.2), (123, 456)]:
        assert add(a, b) == add(b, a)

def test_add_with_nan():
    res = add(float("nan"), 1.0)
    assert math.isnan(res)

# --- subtract ---
@pytest.mark.parametrize("a,b,expected", [
    (5, 3, 2),
    (-4, 9, -13),
    (2.5, 1.0, 1.5),
    (10**12, 1, 10**12 - 1),
])
def test_subtract_basic(a, b, expected):
    assert subtract(a, b) == expected

def test_subtract_decimal():
    d1 = decimal.Decimal("5.00")
    d2 = decimal.Decimal("1.75")
    assert subtract(d1, d2) == decimal.Decimal("3.25")

def test_subtract_relation_with_add():
    # Свойство: a - b == add(a, -b)
    for a, b in [(7, 3), (-2, 5), (0.5, 0.25)]:
        assert subtract(a, b) == add(a, -b)

# --- multiply ---
@pytest.mark.parametrize("a,b,expected", [
    (0, 5, 0),
    (1, 7, 7),
    (-3, 4, -12),
    (-2, -8, 16),
    (2.5, 4, 10.0),
    (10**6, 10**6, 10**12),
])
def test_multiply_basic(a, b, expected):
    assert multiply(a, b) == expected

def test_multiply_commutative():
    for a, b in [(3, 9), (-5, 7), (0.25, 0.5)]:
        assert multiply(a, b) == multiply(b, a)

def test_multiply_decimal():
    d1 = decimal.Decimal("1.20")
    d2 = decimal.Decimal("2.50")
    assert multiply(d1, d2) == decimal.Decimal("3.00")

def test_multiply_distributive_over_add():
    # Распределительность: a*(b+c) == a*b + a*c
    for a, b, c in [(3, 4, 5), (-2, 7, -1), (1.5, 0.2, 0.3)]:
        left = multiply(a, add(b, c))
        right = add(multiply(a, b), multiply(a, c))
        assert left == right

def test_multiply_with_nan():
    res = multiply(float("nan"), 2.0)
    assert math.isnan(res)
