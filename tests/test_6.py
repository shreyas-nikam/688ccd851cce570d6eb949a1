import pytest
from definition_fbb0ebc7d1714d1ab91b1c4dc23fda2a import calculate_error_m2

@pytest.mark.parametrize("var_m2, phi_inv_0_975, expected", [
    (1.0, 1.96, 1.96),
    (4.0, 1.96, 3.92),
    (0.25, 1.96, 0.98),
    (1.0, 0.0, 0.0),
    (0.0, 1.96, 0.0),
])
def test_calculate_error_m2(var_m2, phi_inv_0_975, expected):
    assert calculate_error_m2(var_m2, phi_inv_0_975) == expected
