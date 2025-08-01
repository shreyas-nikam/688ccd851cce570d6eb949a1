import pytest
import numpy as np
from definition_a7a6e7c3c4f44dbcb52ee283d96a65d3 import generate_synthetic_eepe_k_data

@pytest.mark.parametrize("m_runs, mean, std_dev, expected_length", [
    (100, 100, 20, 100),
    (1, 50, 5, 1),
    (0, 0, 0, 0),
])
def test_generate_synthetic_eepe_k_data_length(m_runs, mean, std_dev, expected_length):
    result = generate_synthetic_eepe_k_data(m_runs, mean, std_dev)
    assert len(result) == expected_length

@pytest.mark.parametrize("m_runs, mean, std_dev", [
    (100, 100, 20),
    (1, 50, 5),
])
def test_generate_synthetic_eepe_k_data_type(m_runs, mean, std_dev):
    result = generate_synthetic_eepe_k_data(m_runs, mean, std_dev)
    assert isinstance(result, np.ndarray)
    assert result.dtype == np.float64

def test_generate_synthetic_eepe_k_data_std_dev_zero():
    result = generate_synthetic_eepe_k_data(100, 100, 0)
    assert np.all(result == 100)

def test_generate_synthetic_eepe_k_data_negative_std_dev():
    with pytest.raises(ValueError):
         generate_synthetic_eepe_k_data(100, 100, -1)

def test_generate_synthetic_eepe_k_data_large_m_runs():
    m_runs = 10000
    mean = 100
    std_dev = 20
    result = generate_synthetic_eepe_k_data(m_runs, mean, std_dev)
    assert len(result) == m_runs

