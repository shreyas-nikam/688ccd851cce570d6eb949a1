
import numpy as np
import math

phi_inv_0_975 = 1.96

def generate_synthetic_eepe_k_data(m_runs, mean, std_dev):
    """Generates synthetic EEPE^k data."""
    if std_dev < 0:
        raise ValueError("Standard deviation cannot be negative.")
    if m_runs == 0:
        return np.array([])
    return np.random.normal(mean, std_dev, m_runs)

def generate_synthetic_dj_data(N_scenarios, mean, std_dev):
    """Generates synthetic Dj values."""
    if std_dev < 0:
        raise ValueError("Standard deviation cannot be negative.")
    if N_scenarios == 0:
        return np.array([])
    data = np.random.normal(mean, std_dev, N_scenarios)
    data[data < 0] = 0
    return data

def calculate_var_m1(eepe_k_values):
    """Computes the variance of EEPE based on Method 1."""
    return np.var(eepe_k_values)

def calculate_conv_adj(m_val):
    """Computes the convergence adjustment factor for Method 1."""
    if m_val <= 1:
        # Avoid division by zero and log for m_val = 1
        return float('inf') if m_val == 1 else 0.0 # Placeholder for specific error handling or value
    t_quantile = {
        2: 12.706,
        50: 2.009,
        100: 1.984,
        1000: 1.962
    }
    if m_val in t_quantile:
        adj_factor = t_quantile[m_val] / math.sqrt(m_val)
    else:
        # Use Student's t-distribution approximation for t_quantile for larger m
        # For very large m, t-distribution approaches normal, so 1.96 is a good approximation for 97.5th percentile
        adj_factor = 1.96 / math.sqrt(m_val)
    return adj_factor

def calculate_error_m1(var_m1, conv_adj_val, phi_inv_0_975):
    """Computes the final Monte Carlo error for Method 1."""
    error_m1 = (var_m1**0.5) * conv_adj_val * phi_inv_0_975
    return error_m1

def calculate_var_m2(dj_values):
    """Computes the variance of EEPE based on Method 2."""
    n = len(dj_values)
    if n <= 1:
        return 0.0
    mean = sum(dj_values) / n
    variance = sum([(x - mean) ** 2 for x in dj_values]) / n
    return variance

def calculate_error_m2(var_m2, phi_inv_0_975):
    """Computes the final Monte Carlo error for Method 2."""
    error_m2 = phi_inv_0_975 * (var_m2**0.5)
    return error_m2
