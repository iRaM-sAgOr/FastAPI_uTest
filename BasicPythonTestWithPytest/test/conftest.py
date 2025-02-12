import pytest
"""
This is a conftest.py file for pytest configuration.

The conftest.py file is used to define fixtures that can be shared across multiple test files.
It is automatically discovered by pytest and can be used to provide setup and teardown code for tests.

Fixtures defined in this file can be used by simply including their name as an argument in test functions.

Fixtures:
    width: A fixture that returns a fixed width value of 5.
    So we assume all our rectangle and square will be of width 5.
"""


@pytest.fixture
def width():
    return 5
