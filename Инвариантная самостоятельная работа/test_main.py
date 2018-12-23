import pytest
from main import insertion_sort

@pytest.mark.parametrize("description,unsorted,expected", [
    ("positive", [2, 1, 3, 10], [1, 2, 3, 10]),
    ("negative", [-2, -1, -3, -100], [-100, -3, -2, -1]),
    ("including zero", [2, 0, 1], [0, 1, 2]),
    ("duplicate values", [0, 5, 1, 0, 5], [0, 0, 1, 5, 5]),
    ("floats", [0.1, 0.3, 0.2], [0.1, 0.2, 0.3]),
])
def test_main_sort(description, unsorted, expected):
    assert insertion_sort(unsorted) == expected
