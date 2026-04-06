from app import add, sub, mul, div
def test_add():
    assert add(2, 3) == 5
    assert add(5, 3) == 8
def test_subtract():
    assert sub(5, 3) == 2
    assert sub(0, 0) == 0
def test_multiply():
    assert mul(4, 3) == 12
    assert mul(12, 12) == 144
def test_divide():
    assert div(10, 2) == 5
