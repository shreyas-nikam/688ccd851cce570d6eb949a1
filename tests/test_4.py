import pytest
from definition_3181e847df1844e9a9e9f8fb7c0f6b34 import calculate_error_m1

@pytest.mark.parametrize("var_m1, conv_adj_val, phi_inv_0_975, expected", [
    (1.0, 1.0, 1.96, 1.96),
    (4.0, 1.5, 1.96, 5.88),
    (0.0, 1.0, 1.96, 0.0),
    (9.0, 0.5, 1.96, 2.94),
    (2.25, 1.2, 1.96, 3.528),
])
def test_calculate_error_m1(var_m1, conv_adj_val, phi_inv_0_975, expected):
    result = calculate_error_m1(var_m1, conv_adj_val, phi_inv_0_975)
    assert result == expected
