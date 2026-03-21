from src.calculator import add, subtract
def test_add():
    assert add(2, 3) == 5
def test_subtract():
    assert subtract(5, 2) == 3
from src.calculator import power

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(2, -1) == 0.5
    