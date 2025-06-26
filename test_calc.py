import calculator
import pytest

def test_add():
    assert calculator.add(2,3) == 5

def test_ub():
    assert calculator.sub(4,2) == 2

def test_mult():
    assert calculator.mult(4,2) == 8

def test_div_zero():
    with pytest.raises(ValueError, match="Cannot divide by 0"):
        calculator.div(5,0)