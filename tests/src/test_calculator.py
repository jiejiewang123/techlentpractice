from app.src.calculator import Calculator

cal = Calculator()

def test_add():
    assert cal.add(1, 1) == 2
    assert cal.add(1, 2) == 3

def test_subtract():
    assert cal.substract(3, 5) == -2

    assert cal.substract(6, 1) == 5

    assert cal.substract(2, 1) == 1


