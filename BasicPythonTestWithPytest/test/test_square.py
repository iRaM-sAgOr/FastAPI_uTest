import pytest
from source.square import Square


def test_square_area(width):
    square = Square("Square", width)
    assert square.area() == 25


def test_square_perimeter(width):
    square = Square("Square", width)
    assert square.perimeter() == 20


@pytest.mark.parametrize("side, result", [(3, 12), (4, 16), (5, 20)])
def test_square_perimeter_parametrize(width, side, result):
    square = Square("Square", side)
    assert square.perimeter() == result