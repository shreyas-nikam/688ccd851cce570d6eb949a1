import pytest
from definition_a22536ed1b0f4edc9b2104e7566cf55f import generate_synthetic_dj_data
import numpy as np

def test_generate_synthetic_dj_data_positive_scenarios():
    """Test that the function returns an array of the correct size with positive values."""
    N_scenarios = 10
    mean = 100
    std_dev = 20
    data = generate_synthetic_dj_data(N_scenarios, mean, std_dev)
    assert len(data) == N_scenarios
    assert np.all(data >= 0)  # Assuming exposures cannot be negative

def test_generate_synthetic_dj_data_zero_std_dev():
    """Test that the function returns an array with all values equal to the mean when std_dev is zero."""
    N_scenarios = 5
    mean = 50
    std_dev = 0
    data = generate_synthetic_dj_data(N_scenarios, mean, std_dev)
    assert len(data) == N_scenarios
    assert np.all(data == mean)

def test_generate_synthetic_dj_data_large_values():
    """Test the function with large mean and std_dev to check for overflow issues."""
    N_scenarios = 20
    mean = 1e9
    std_dev = 1e8
    data = generate_synthetic_dj_data(N_scenarios, mean, std_dev)
    assert len(data) == N_scenarios
    assert np.all(data >= 0) # Assuming exposures can't be negative.

def test_generate_synthetic_dj_data_zero_scenarios():
     """Test that the function returns an empty array when N_scenarios is zero."""
     N_scenarios = 0
     mean = 100
     std_dev = 20
     data = generate_synthetic_dj_data(N_scenarios, mean, std_dev)
     assert len(data) == N_scenarios

def test_generate_synthetic_dj_data_negative_std_dev():
    """Test that the function raises a ValueError when std_dev is negative."""
    N_scenarios = 10
    mean = 100
    std_dev = -20
    with pytest.raises(ValueError):
        generate_synthetic_dj_data(N_scenarios, mean, std_dev)
