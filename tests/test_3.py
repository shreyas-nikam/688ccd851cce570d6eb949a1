import pytest
from definition_c09d391f7ac04987a64a77d74bec0d11 import calculate_conv_adj
import math

@pytest.mark.parametrize("m_val, expected", [
    (50, 1.0135),
    (2, 12.706),
    (100, 1.007),
    (1000, 1.0007),
    (1, ValueError)
])
def test_calculate_conv_adj(m_val, expected):
    if m_val == 1:
        with pytest.raises(ValueError):
            calculate_conv_adj(m_val)
    else:
        result = calculate_conv_adj(m_val)
        assert math.isclose(result, expected, rel_tol=1e-3)

