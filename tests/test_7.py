import pytest
from definition_fb8c8abc871b4f18bcdc032a611af5dd import plot_method1_error
import matplotlib.pyplot as plt
import numpy as np

def test_plot_method1_error_typical():
    m_values = np.array([10, 20, 30, 40, 50])
    errors_m1 = np.array([0.5, 0.4, 0.3, 0.2, 0.1])
    plot_method1_error(m_values, errors_m1)
    assert plt.gca().get_xlabel() == "Number of MC Runs ($m$)", "X-axis label incorrect"
    assert plt.gca().get_ylabel() == "Calculated $\\text{error}_{m1}(\\text{EEPE})$", "Y-axis label incorrect"
    assert plt.gca().get_title() == "Method 1: EEPE Monte Carlo Error vs. Number of MC Runs ($m$)", "Title incorrect"
    plt.close()

def test_plot_method1_error_empty():
    m_values = np.array([])
    errors_m1 = np.array([])
    plot_method1_error(m_values, errors_m1)
    assert plt.gca().get_xlabel() == "Number of MC Runs ($m$)", "X-axis label incorrect"
    assert plt.gca().get_ylabel() == "Calculated $\\text{error}_{m1}(\\text{EEPE})$", "Y-axis label incorrect"
    assert plt.gca().get_title() == "Method 1: EEPE Monte Carlo Error vs. Number of MC Runs ($m$)", "Title incorrect"
    plt.close()

def test_plot_method1_error_single_point():
    m_values = np.array([10])
    errors_m1 = np.array([0.5])
    plot_method1_error(m_values, errors_m1)
    assert plt.gca().get_xlabel() == "Number of MC Runs ($m$)", "X-axis label incorrect"
    assert plt.gca().get_ylabel() == "Calculated $\\text{error}_{m1}(\\text{EEPE})$", "Y-axis label incorrect"
    assert plt.gca().get_title() == "Method 1: EEPE Monte Carlo Error vs. Number of MC Runs ($m$)", "Title incorrect"
    plt.close()

def test_plot_method1_error_different_lengths():
    m_values = np.array([10, 20, 30])
    errors_m1 = np.array([0.5, 0.4])
    with pytest.raises(ValueError):
        plot_method1_error(m_values, errors_m1)
    plt.close()

def test_plot_method1_error_non_numeric_values():
    m_values = np.array(['a', 'b', 'c'])
    errors_m1 = np.array(['x', 'y', 'z'])
    with pytest.raises(TypeError):
        plot_method1_error(m_values, errors_m1)
    plt.close()
