
import streamlit as st
import numpy as np
import plotly.graph_objects as go
from application_pages.utils import (
    phi_inv_0_975,
    generate_synthetic_eepe_k_data,
    calculate_var_m1,
    calculate_conv_adj,
    calculate_error_m1
)

def run_page1():
    st.title("Method 1: EEPE Monte Carlo Error Estimation")
    st.markdown(r"""
    Method 1 calculates the Monte Carlo error of EEPE based on multiple independent Monte Carlo runs.
    The formula for the error is:
    $$ \text{error}_{m1}(\text{EEPE}) = \sqrt{\text{var}_{m1}(\text{EEPE})} \times \text{convAdj}(m) \times \Phi^{-1}(0.975) $$
    where $\text{var}_{m1}(\text{EEPE})$ is the sample variance of $\text{EEPE}^k$ values, and $\text{convAdj}(m)$ is the convergence adjustment factor:
    $$ \text{convAdj}(m) = \frac{t_{m-1, 0.975}}{\sqrt{m}} $$
    """)

    st.sidebar.header("Method 1 Parameters")
    synthetic_mean = st.sidebar.slider(
        "Synthetic Data Mean (μ)",
        min_value=1, max_value=500, value=100, step=1,
        help="Sets the average value for the generated synthetic EEPE or exposure data."
    )
    synthetic_volatility = st.sidebar.slider(
        "Synthetic Data Volatility (σ)",
        min_value=1, max_value=100, value=10, step=1,
        help="Sets the variability (standard deviation) of the generated synthetic EEPE or exposure data."
    )
    m_runs = st.sidebar.slider(
        "Number of MC Runs for Calculations (m)",
        min_value=2, max_value=1000, value=50, step=1,
        help="Number of Monte Carlo runs ($m$) used to estimate $\text{EEPE}^k$ for Method 1."
    )
    conv_adj_plot_max_m = st.sidebar.slider(
        "Max M for Convergence Plot",
        min_value=20, max_value=5000, value=1000, step=10,
        help="Sets the upper limit for the 'Number of MC Runs ($m$)' axis in Method 1 convergence plots."
    )

    # Calculate single error value
    eepe_k_data = generate_synthetic_eepe_k_data(m_runs, synthetic_mean, synthetic_volatility)
    if eepe_k_data.size > 1:
        var_m1_val = calculate_var_m1(eepe_k_data)
        conv_adj_val = calculate_conv_adj(m_runs)
        error_m1_val = calculate_error_m1(var_m1_val, conv_adj_val, phi_inv_0_975)
        st.markdown(f"**Calculated $\text{{error}}_{{m1}}(\text{{EEPE}})$ for $m={m_runs}$:  {error_m1_val:.4f}**")
    else:
        st.write("Not enough data to calculate error for Method 1. Increase 'Number of MC Runs'.")
        error_m1_val = 0.0

    st.divider()

    # Plot Method 1 EEPE Monte Carlo Error vs. Number of MC Runs (m)
    st.subheader("Method 1: EEPE Monte Carlo Error vs. Number of MC Runs ($m$)")
    m_values_plot = np.arange(2, conv_adj_plot_max_m + 1, max(1, conv_adj_plot_max_m // 100))
    errors_m1_plot = []
    for m in m_values_plot:
        data_for_plot = generate_synthetic_eepe_k_data(m, synthetic_mean, synthetic_volatility)
        if data_for_plot.size > 1:
            var_m1_plot = calculate_var_m1(data_for_plot)
            conv_adj_plot = calculate_conv_adj(m)
            errors_m1_plot.append(calculate_error_m1(var_m1_plot, conv_adj_plot, phi_inv_0_975))
        else:
            errors_m1_plot.append(0.0) # Handle cases where m is too small for variance

    fig_m1_error = go.Figure(data=go.Scatter(x=m_values_plot, y=errors_m1_plot, mode='lines'))
    fig_m1_error.update_layout(
        title='Method 1: EEPE Monte Carlo Error vs. Number of MC Runs ($m$)',
        xaxis_title='Number of MC Runs ($m$)',
        yaxis_title='Calculated $\text{error}_{m1}(\text{EEPE})$'
    )
    st.plotly_chart(fig_m1_error, use_container_width=True)

    st.divider()

    # Plot Impact of m on Convergence Adjustment Factor
    st.subheader("Impact of $m$ on Convergence Adjustment Factor")
    conv_adj_values_plot = [calculate_conv_adj(m) if m > 1 else 0.0 for m in m_values_plot] # Handle m=1 or less
    
    fig_conv_adj = go.Figure(data=go.Scatter(x=m_values_plot, y=conv_adj_values_plot, mode='lines'))
    fig_conv_adj.update_layout(
        title='Impact of m on Convergence Adjustment Factor',
        xaxis_title='Number of MC Runs ($m$)',
        yaxis_title='Convergence Adjustment Factor ($\text{convAdj}(m)$)'
    )
    st.plotly_chart(fig_conv_adj, use_container_width=True)
