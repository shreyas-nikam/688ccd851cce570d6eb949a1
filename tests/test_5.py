import pytest
from definition_e2e929ae9a2843f0893126404b90629a import calculate_var_m2

@pytest.mark.parametrize("input_data, expected", [
    ([1, 2, 3, 4, 5], 2.5),
    ([10, 10, 10, 10, 10], 0.0),
    ([1, 2, 3, 4, 10], 10.3),
    ([-1, -2, -3, -4, -5], 2.5),
    ([1], 0.0)
])
def test_calculate_var_m2(input_data, expected):
    assert calculate_var_m2(input_data) == expected
