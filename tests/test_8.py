import pytest
from definition_724e19395c93459bbb02760b8e929629 import plot_method2_error
import matplotlib.pyplot as plt
import numpy as np

def test_plot_method2_error_valid_input():
    N_values = np.array([100, 200, 300])
    errors_m2 = np.array([0.1, 0.05, 0.02])
    
    try:
        plot_method2_error(N_values, errors_m2)
        plt.close()
    except Exception as e:
        assert False, f"Plotting failed with exception: {e}"

def test_plot_method2_error_empty_input():
    N_values = np.array([])
    errors_m2 = np.array([])

    try:
        plot_method2_error(N_values, errors_m2)
        plt.close()
    except Exception as e:
        assert False, f"Plotting failed with exception: {e}"

def test_plot_method2_error_different_lengths():
    N_values = np.array([100, 200])
    errors_m2 = np.array([0.1, 0.05, 0.02])
    
    with pytest.raises(ValueError):
       plot_method2_error(N_values, errors_m2)

def test_plot_method2_error_non_numeric_input():
    N_values = np.array(['a', 'b', 'c'])
    errors_m2 = np.array([0.1, 0.05, 0.02])

    with pytest.raises(TypeError):
        plot_method2_error(N_values, errors_m2)

def test_plot_method2_error_inf_values():
    N_values = np.array([100, 200, 300])
    errors_m2 = np.array([np.inf, 0.05, 0.02])
    
    try:
        plot_method2_error(N_values, errors_m2)
        plt.close()
    except Exception as e:
        assert False, f"Plotting failed with exception: {e}"

