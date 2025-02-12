import pytest
from source.circle import Circle


@pytest.fixture
def radius():
    return 5


def test_circle_area(radius):
    circular = Circle("Circle", radius)
    assert circular.area() == 78.53975


def test_circle_perimeter(radius):
    circular = Circle("Circle", radius)
    assert circular.perimeter() == 31.4159


def test_circle_area_exception():
    circular = Circle("Circle", 0)
    with pytest.raises(ValueError):
        circular.area()


def test_circle_perimeter_exception():
    circular = Circle("Circle", 0)
    with pytest.raises(ValueError):
        circular.perimeter()


@pytest.mark.parametrize("radius, result", [(3, 28.27431), (4, 50.26544)])
def test_circle_area_parametrize(radius, result):
    circular = Circle("Circle", radius)
    assert circular.area() == result