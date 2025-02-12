import pytest
from source.rectangle import Rectangle


def test_rectangle_area(width):
    # here width is a fixture that returns a fixed width value of 5
    rectangular = Rectangle("Rectangle", 3, width)
    assert rectangular.area() == 15


def test_rectangle_perimeter(width):
    # here width is a fixture that returns a fixed width value of 5
    rectangular = Rectangle("Rectangle", 3, width)
    assert rectangular.perimeter() == 16


@pytest.mark.parametrize("length, result", [(3, 16), (4, 18), (5, 20)])
def test_rectangle_perimeter_parametrize(width, length, result):
    # here width is a fixture that returns a fixed width value of 5
    rectangular = Rectangle("Rectangle", length, width)
    assert rectangular.perimeter() == result


def test_rectangle_area_exception():
    rectangular = Rectangle("Rectangle", 0, 0)
    with pytest.raises(ValueError):
        rectangular.area()


# now we will describe some more test cases considering some specific cases
# we will use some pytest markers to skip, xfail, skipif, and slow down the test cases
@pytest.mark.skip(reason="Skipping this test for demonstration purposes")
def test_rectangle_skip():
    rectangular = Rectangle("Rectangle", 3, 5)
    assert rectangular.area() == 15


@pytest.mark.xfail(reason="This test is expected to fail")
def test_rectangle_xfail():
    rectangular = Rectangle("Rectangle", 3, 5)
    assert rectangular.area() == 20  # This assertion is intentionally incorrect


@pytest.mark.skipif(True, reason="Skipping this test based on a condition")
def test_rectangle_skipif():
    rectangular = Rectangle("Rectangle", 3, 5)
    assert rectangular.perimeter() == 16


# @pytest.mark.slow
# def test_rectangle_slow():
#     rectangular = Rectangle("Rectangle", 3, 5)
#     assert rectangular.area() == 15