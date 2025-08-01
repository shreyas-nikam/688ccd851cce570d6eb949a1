import pytest
from definition_5e9bcbe51e4949dc88d87ba4dfd156ff import plot_comparison_error
import matplotlib.pyplot as plt
from unittest.mock import patch

@patch('matplotlib.pyplot.bar')
@patch('matplotlib.pyplot.title')
@patch('matplotlib.pyplot.xlabel')
@patch('matplotlib.pyplot.ylabel')
@patch('matplotlib.pyplot.xticks')
@patch('matplotlib.pyplot.show')
def test_plot_comparison_error_valid_input(mock_show, mock_xticks, mock_ylabel, mock_xlabel, mock_title, mock_bar):
    """Test that the function calls plotting functions with correct data."""
    error_m1 = 0.1
    error_m2 = 0.2
    plot_comparison_error(error_m1, error_m2)

    mock_bar.assert_called_once_with(['Method 1', 'Method 2'], [error_m1, error_m2])
    mock_title.assert_called_once_with('Comparison of EEPE MC Error (Method 1 vs. Method 2)')
    mock_xlabel.assert_called_once_with('Method')
    mock_ylabel.assert_called_once_with('Calculated EEPE MC Error')
    mock_xticks.assert_called_once_with(['Method 1', 'Method 2'])
    mock_show.assert_called_once()

@patch('matplotlib.pyplot.bar')
@patch('matplotlib.pyplot.title')
@patch('matplotlib.pyplot.xlabel')
@patch('matplotlib.pyplot.ylabel')
@patch('matplotlib.pyplot.xticks')
@patch('matplotlib.pyplot.show')
def test_plot_comparison_error_zero_errors(mock_show, mock_xticks, mock_ylabel, mock_xlabel, mock_title, mock_bar):
    """Test with zero error values."""
    error_m1 = 0.0
    error_m2 = 0.0
    plot_comparison_error(error_m1, error_m2)

    mock_bar.assert_called_once_with(['Method 1', 'Method 2'], [error_m1, error_m2])

@patch('matplotlib.pyplot.bar')
@patch('matplotlib.pyplot.title')
@patch('matplotlib.pyplot.xlabel')
@patch('matplotlib.pyplot.ylabel')
@patch('matplotlib.pyplot.xticks')
@patch('matplotlib.pyplot.show')
def test_plot_comparison_error_negative_errors(mock_show, mock_xticks, mock_ylabel, mock_xlabel, mock_title, mock_bar):
    """Test with negative error values (should still plot)."""
    error_m1 = -0.1
    error_m2 = -0.2
    plot_comparison_error(error_m1, error_m2)
    mock_bar.assert_called_once_with(['Method 1', 'Method 2'], [error_m1, error_m2])

@patch('matplotlib.pyplot.bar')
@patch('matplotlib.pyplot.title')
@patch('matplotlib.pyplot.xlabel')
@patch('matplotlib.pyplot.ylabel')
@patch('matplotlib.pyplot.xticks')
@patch('matplotlib.pyplot.show')
def test_plot_comparison_error_large_errors(mock_show, mock_xticks, mock_ylabel, mock_xlabel, mock_title, mock_bar):
    """Test with large error values."""
    error_m1 = 1000.0
    error_m2 = 2000.0
    plot_comparison_error(error_m1, error_m2)
    mock_bar.assert_called_once_with(['Method 1', 'Method 2'], [error_m1, error_m2])

@patch('matplotlib.pyplot.bar')
@patch('matplotlib.pyplot.title')
@patch('matplotlib.pyplot.xlabel')
@patch('matplotlib.pyplot.ylabel')
@patch('matplotlib.pyplot.xticks')
@patch('matplotlib.pyplot.show')
def test_plot_comparison_error_one_error_zero(mock_show, mock_xticks, mock_ylabel, mock_xlabel, mock_title, mock_bar):
    """Test with one of the error values being zero."""
    error_m1 = 0.5
    error_m2 = 0.0
    plot_comparison_error(error_m1, error_m2)
    mock_bar.assert_called_once_with(['Method 1', 'Method 2'], [error_m1, error_m2])
