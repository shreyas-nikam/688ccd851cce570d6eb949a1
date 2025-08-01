import pytest
from definition_c175a0e2630c4c98ada4cb06e87d5219 import calculate_var_m1
import numpy as np

@pytest.mark.parametrize("input, expected", [
    ([1, 2, 3], 1),
    ([5, 5, 5, 5, 5], 0),
    ([10, 20, 30], 100),
    ([1.0, 2.0, 3.0], 1.0),
    ([1, 100], 2450.25),
])
def test_calculate_var_m1(input, expected):
    assert np.isclose(calculate_var_m1(input), expected)
