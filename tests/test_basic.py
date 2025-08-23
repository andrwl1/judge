import math
from judge import add
import decimal
import pytest

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
