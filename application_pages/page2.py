
import streamlit as st
import numpy as np
import plotly.graph_objects as go
from application_pages.utils import (
    phi_inv_0_975,
    generate_synthetic_dj_data,
    calculate_var_m2,
    calculate_error_m2
)

def run_page2():
    st.title("Method 2: EEPE Monte Carlo Error Estimation")
    st.markdown(r"""
    Method 2 calculates the Monte Carlo error of EEPE based on the variance of individual discounted positive exposures $D_j$.
    The formula for the error is:
    $$ \text{error}_{m2}(\text{EEPE}) = \sqrt{\text{var}_{m2}(\text{EEPE})} \times \Phi^{-1}(0.975) $$
    where $\text{var}_{m2}(\text{EEPE})$ is the sample variance of $D_j$ values:
    $$ \text{var}_{m2}(\text{EEPE}) = \frac{1}{N} \sum_{j=1}^{N} (D_j - \bar{D})^2 $$
    and $D_j = \max(0, X_j)$ where $X_j \sim \mathcal{N}(\mu, \sigma^2)$.
    """)

    st.sidebar.header("Method 2 Parameters")
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
    N_scenarios = st.sidebar.slider(
        "Number of Scenarios for Calculations (N)",
        min_value=100, max_value=100000, value=10000, step=100,
        help="Number of scenarios ($N$) used to generate $D_j$ values for Method 2."
    )
    N_plot_max_N = st.sidebar.slider(
        "Max N for Convergence Plot",
        min_value=1000, max_value=1000000, value=100000, step=1000,
        help="Sets the upper limit for the 'Number of Scenarios ($N$)' axis in Method 2 convergence plots."
    )

    # Calculate single error value
    dj_data = generate_synthetic_dj_data(N_scenarios, synthetic_mean, synthetic_volatility)
    if dj_data.size > 1:
        var_m2_val = calculate_var_m2(dj_data)
        error_m2_val = calculate_error_m2(var_m2_val, phi_inv_0_975)
        st.markdown(f"**Calculated $\text{{error}}_{{m2}}(\text{{EEPE}})$ for $N={N_scenarios}$: {error_m2_val:.4f}**")
    else:
        st.write("Not enough data to calculate error for Method 2. Increase 'Number of Scenarios'.")
        error_m2_val = 0.0

    st.divider()

    # Plot Method 2 EEPE Monte Carlo Error vs. Number of Scenarios (N)
    st.subheader("Method 2: EEPE Monte Carlo Error vs. Number of Scenarios ($N$)")
    N_values_plot = np.arange(100, N_plot_max_N + 1, max(100, N_plot_max_N // 100))
    errors_m2_plot = []
    for N in N_values_plot:
        data_for_plot = generate_synthetic_dj_data(N, synthetic_mean, synthetic_volatility)
        if data_for_plot.size > 1:
            var_m2_plot = calculate_var_m2(data_for_plot)
            errors_m2_plot.append(calculate_error_m2(var_m2_plot, phi_inv_0_975))
        else:
            errors_m2_plot.append(0.0)

    fig_m2_error = go.Figure(data=go.Scatter(x=N_values_plot, y=errors_m2_plot, mode='lines'))
    fig_m2_error.update_layout(
        title='Method 2: EEPE Monte Carlo Error vs. Number of Scenarios ($N$)',
        xaxis_title='Number of Scenarios ($N$)',
        yaxis_title='Calculated $\text{error}_{m2}(\text{EEPE})$'
    )
    st.plotly_chart(fig_m2_error, use_container_width=True)
