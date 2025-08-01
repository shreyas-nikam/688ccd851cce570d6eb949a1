
import streamlit as st
import numpy as np
import plotly.graph_objects as go
from application_pages.utils import (
    phi_inv_0_975,
    generate_synthetic_eepe_k_data,
    calculate_var_m1,
    calculate_conv_adj,
    calculate_error_m1,
    generate_synthetic_dj_data,
    calculate_var_m2,
    calculate_error_m2
)

def run_page3():
    st.title("Comparison of Monte Carlo Error Estimation Methods")
    st.markdown("This page allows for a direct comparison of the calculated Monte Carlo errors from Method 1 and Method 2 using a consistent set of parameters.")

    st.sidebar.header("Comparison Parameters")
    synthetic_mean = st.sidebar.slider(
        "Synthetic Data Mean (μ)",
        min_value=1, max_value=500, value=100, step=1, key="comp_mean",
        help="Sets the average value for the generated synthetic EEPE or exposure data."
    )
    synthetic_volatility = st.sidebar.slider(
        "Synthetic Data Volatility (σ)",
        min_value=1, max_value=100, value=10, step=1, key="comp_volatility",
        help="Sets the variability (standard deviation) of the generated synthetic EEPE or exposure data."
    )
    m_runs_comp = st.sidebar.slider(
        "Number of MC Runs for Method 1 (m)",
        min_value=2, max_value=1000, value=50, step=1, key="comp_m_runs",
        help="Number of Monte Carlo runs ($m$) used for Method 1 in the comparison."
    )
    N_scenarios_comp = st.sidebar.slider(
        "Number of Scenarios for Method 2 (N)",
        min_value=100, max_value=100000, value=10000, step=100, key="comp_N_scenarios",
        help="Number of scenarios ($N$) used for Method 2 in the comparison."
    )

    # Calculate Method 1 Error
    eepe_k_data_comp = generate_synthetic_eepe_k_data(m_runs_comp, synthetic_mean, synthetic_volatility)
    if eepe_k_data_comp.size > 1:
        var_m1_comp = calculate_var_m1(eepe_k_data_comp)
        conv_adj_comp = calculate_conv_adj(m_runs_comp)
        error_m1_comp = calculate_error_m1(var_m1_comp, conv_adj_comp, phi_inv_0_975)
    else:
        error_m1_comp = 0.0
        st.warning("Not enough data for Method 1 calculation in comparison.")

    # Calculate Method 2 Error
    dj_data_comp = generate_synthetic_dj_data(N_scenarios_comp, synthetic_mean, synthetic_volatility)
    if dj_data_comp.size > 1:
        var_m2_comp = calculate_var_m2(dj_data_comp)
        error_m2_comp = calculate_error_m2(var_m2_comp, phi_inv_0_975)
    else:
        error_m2_comp = 0.0
        st.warning("Not enough data for Method 2 calculation in comparison.")

    st.markdown(f"**Method 1 Error ($	ext{{error}}_{{m1}}(\text{{EEPE}})$) for $m={m_runs_comp}$: {error_m1_comp:.4f}**")
    st.markdown(f"**Method 2 Error ($	ext{{error}}_{{m2}}(\text{{EEPE}})$) for $N={N_scenarios_comp}$: {error_m2_comp:.4f}**")

    st.divider()

    # Comparison Bar Chart
    st.subheader("Comparison of EEPE MC Error (Method 1 vs. Method 2)")
    methods = ['Method 1', 'Method 2']
    errors = [error_m1_comp, error_m2_comp]

    fig_comparison = go.Figure(data=[go.Bar(x=methods, y=errors)])
    fig_comparison.update_layout(
        title='Comparison of EEPE MC Error (Method 1 vs. Method 2)',
        xaxis_title='Method',
        yaxis_title='Calculated EEPE MC Error'
    )
    st.plotly_chart(fig_comparison, use_container_width=True)
