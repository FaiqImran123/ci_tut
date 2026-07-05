from app import calculate


def test_positive_number():
    square, cube = calculate(2)
    assert square == 4
    assert cube == 8


def test_zero():
    square, cube = calculate(0)
    assert square == 0
    assert cube == 0


def test_negative_number():
    square, cube = calculate(-3)
    assert square == 9
    assert cube == -27


def test_float_number():
    square, cube = calculate(2.5)
    assert square == 6.25
    assert cube == 15.625