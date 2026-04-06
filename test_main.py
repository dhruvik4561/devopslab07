from app import add, sub, mul, div

def test_add():
    assert add(2, 3) == 5

def test_sub():
    assert sub(20,5) == 15

def test_mul():
    assert mul(5,2) == 10

def test_div():
    assert div(10,5) == 2