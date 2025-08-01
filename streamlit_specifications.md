
# Streamlit Application Requirements Specification

## 1. Application Overview

**Purpose and Objectives:**
This Streamlit application aims to provide an interactive platform for users to understand, implement, and compare two distinct methodologies (Method 1 and Method 2) for estimating the Monte Carlo (MC) error of Expected Positive Exposure (EEPE) in counterparty credit risk. The application will allow users to manipulate key simulation parameters and observe their direct impact on error estimates and convergence behavior.

The primary objectives are:
*   To enable users to understand and implement the calculations for $\text{error}_{m1}(\text{EEPE})$ and $\text{error}_{m2}(\text{EEPE})$.
*   To visualize the relationship between simulation parameters (number of MC runs $m$, number of scenarios $N$) and the calculated Monte Carlo errors.
*   To compare the error magnitudes derived from both Method 1 and Method 2.
*   To illustrate the impact of the convergence adjustment factor $\text{convAdj}(m)$ on Method 1's error.
*   To provide an intuitive, interactive experience for exploring the sensitivities of EEPE error estimation.

**Business Value:**
Understanding and accurately calculating Monte Carlo error in EEPE is critical for regulatory compliance and sound risk management in financial institutions. This application offers a hands-on tool to explore different methodologies and their sensitivities, enabling better model validation, risk assessment, and resource allocation for computationally intensive simulations.

## 2. User Interface Requirements

**Layout and Navigation Structure:**
The application will feature a clear layout with input controls typically placed in a sidebar for easy access and the main content area dedicated to displaying results and visualizations.

**Input Widgets and Controls:**
Users will interact with the application through the following widgets:
*   **Method Selection:** A radio button or dropdown widget to choose between "Method 1" and "Method 2". This selection will dynamically update the visible input sliders and output visualizations.
    *   *Help Text:* "Select the Monte Carlo error estimation method to explore."
*   **General Synthetic Data Parameters (Visible for both methods):**
    *   **Synthetic Data Mean (`synthetic_mean`):** A slider to define the mean of the synthetic EEPE/exposure data.
        *   *Range:* Appropriate numerical range (e.g., 1 to 500, with a default of 100 or 50).
        *   *Help Text:* "Sets the average value for the generated synthetic EEPE or exposure data."
    *   **Synthetic Data Volatility (`synthetic_volatility`):** A slider to define the standard deviation of the synthetic EEPE/exposure data.
        *   *Range:* Appropriate numerical range (e.g., 1 to 100, with a default of 10 or 20).
        *   *Help Text:* "Sets the variability (standard deviation) of the generated synthetic EEPE or exposure data."
*   **Method 1 Specific Parameters (Visible when Method 1 is selected):**
    *   **Number of MC Runs for Calculations (`m_runs`):** A slider to specify the number of Monte Carlo runs ($m$) for Method 1 error calculation and display of the single calculated error.
        *   *Range:* E.g., 2 to 1000, with a default of 50.
        *   *Help Text:* "Number of Monte Carlo runs ($m$) used to estimate $\text{EEPE}^k$ for Method 1."
    *   **Max M for Convergence Plot (`conv_adj_plot_max_m`):** A slider or number input to define the maximum value of $m$ for the Method 1 error convergence plot and $\text{convAdj}(m)$ impact plot.
        *   *Range:* E.g., 20 to 5000, with a default of 1000.
        *   *Help Text:* "Sets the upper limit for the 'Number of MC Runs ($m$)' axis in Method 1 convergence plots."
*   **Method 2 Specific Parameters (Visible when Method 2 is selected):**
    *   **Number of Scenarios for Calculations (`N_scenarios`):** A slider to specify the number of scenarios ($N$) for Method 2 error calculation and display of the single calculated error.
        *   *Range:* E.g., 100 to 100000, with a default of 10000.
        *   *Help Text:* "Number of scenarios ($N$) used to generate $D_j$ values for Method 2."
    *   **Max N for Convergence Plot (`N_plot_max_N`):** A slider or number input to define the maximum value of $N$ for the Method 2 error convergence plot.
        *   *Range:* E.g., 1000 to 1000000, with a default of 100000.
        *   *Help Text:* "Sets the upper limit for the 'Number of Scenarios ($N$)' axis in Method 2 convergence plots."

**Visualization Components:**
The main content area will display the following dynamic visualizations and numerical results:
*   **Calculated Error Value:** A prominent display of the calculated $\text{error}_{m1}(\text{EEPE})$ or $\text{error}_{m2}(\text{EEPE})$ based on the selected method and input parameters.
*   **Method 1: EEPE Monte Carlo Error vs. Number of MC Runs ($m$) Plot:** A line plot showing how $\text{error}_{m1}(\text{EEPE})$ changes as $m$ varies over a predefined or user-selected range.
*   **Method 2: EEPE Monte Carlo Error vs. Number of Scenarios ($N$) Plot:** A line plot showing how $\text{error}_{m2}(\text{EEPE})$ changes as $N$ varies over a predefined or user-selected range.
*   **Comparison of EEPE MC Error (Method 1 vs. Method 2) Bar Chart:** A bar chart comparing the calculated $\text{error}_{m1}(\text{EEPE})$ and $\text{error}_{m2}(\text{EEPE})$ for the currently selected `m_runs` and `N_scenarios`.
*   **Impact of $m$ on Convergence Adjustment Factor Plot:** A line plot showing $\text{convAdj}(m)$ as a function of $m$.

**Interactive Elements and Feedback Mechanisms:**
*   All plots and numerical results will update in real-time as users adjust the sliders or dropdowns.
*   Inline help text and tooltips will be provided for all input controls to explain their purpose and relevance to the calculations as per the user requirements.

## 3. Additional Requirements

**Real-time Updates and Responsiveness:**
The application must be highly responsive, with all calculations and visualizations updating dynamically and in real-time whenever a user modifies an input parameter (e.g., slider value, method selection). This ensures a fluid and interactive learning experience.

**Annotation and Tooltip Specifications:**
Every input widget and control must include inline help text or tooltips. These annotations will briefly describe the purpose of the control, its associated variable (e.g., $m$, $N$, $\mu$, $\sigma$), and its role in the Monte Carlo error calculation, drawing directly from the provided notebook content.

## 4. Notebook Content and Code Requirements

This section outlines the specific Python functions and mathematical formulas from the Jupyter notebook that will be integrated into the Streamlit application.

**Global Constants:**
The constant $\Phi^{-1}(0.975)$ (inverse cumulative function of a standard normal distribution at the 97.5th percentile) is used throughout the error calculations.
*   **Name:** `phi_inv_0_975`
*   **Value:** `1.96`

**Core Functions:**

1.  **`generate_synthetic_eepe_k_data(m_runs, mean, std_dev)`**
    *   **Purpose:** Generates synthetic EEPE values for Method 1, representing $\text{EEPE}^k$ from multiple Monte Carlo runs.
    *   **Parameters:**
        *   `m_runs`: Number of Monte Carlo runs ($m$) to simulate.
        *   `mean`: Mean of the synthetic EEPE data ($\mu$).
        *   `std_dev`: Standard deviation of the synthetic EEPE data ($\sigma$).
    *   **Returns:** A NumPy array of synthetic $\text{EEPE}^k$ values.
    *   **Mathematical Concept:**
        $$ \text{EEPE}^k \sim \mathcal{N}(\mu, \sigma^2) $$
    *   **Code Integration:**
        ```python
        import numpy as np

        def generate_synthetic_eepe_k_data(m_runs, mean, std_dev):
            """Generates synthetic EEPE^k data."""
            if std_dev < 0:
                raise ValueError("Standard deviation cannot be negative.")
            if m_runs == 0:
                return np.array([])
            return np.random.normal(mean, std_dev, m_runs)
        ```

2.  **`generate_synthetic_dj_data(N_scenarios, mean, std_dev)`**
    *   **Purpose:** Generates synthetic discounted positive exposure values ($D_j$) for Method 2, ensuring non-negativity.
    *   **Parameters:**
        *   `N_scenarios`: Number of scenarios ($N$) to simulate.
        *   `mean`: Mean of the synthetic exposure data ($\mu$).
        *   `std_dev`: Standard deviation of the synthetic exposure data ($\sigma$).
    *   **Returns:** A NumPy array of synthetic $D_j$ values.
    *   **Mathematical Concept:**
        $$ D_j = \max(0, X_j) \quad \text{where} \quad X_j \sim \mathcal{N}(\mu, \sigma^2) $$
    *   **Code Integration:**
        ```python
        import numpy as np

        def generate_synthetic_dj_data(N_scenarios, mean, std_dev):
            """Generates synthetic Dj values."""
            if std_dev < 0:
                raise ValueError("Standard deviation cannot be negative.")
            if N_scenarios == 0:
                return np.array([])
            data = np.random.normal(mean, std_dev, N_scenarios)
            data[data < 0] = 0  # Ensure no negative values
            return data
        ```

3.  **`calculate_var_m1(eepe_k_values)`**
    *   **Purpose:** Computes the sample variance of $\text{EEPE}^k$ values based on Method 1.
    *   **Parameters:**
        *   `eepe_k_values`: A NumPy array of synthetic $\text{EEPE}^k$ values.
    *   **Returns:** The calculated variance ($\text{var}_{m1}(\text{EEPE})$).
    *   **Mathematical Concept:**
        $$ \text{var}_{m1}(\text{EEPE}) = \frac{1}{m-1} \sum_{k=1}^{m} (\text{EEPE}^k - \bar{EEPE})^2 $$
    *   **Code Integration:**
        ```python
        import numpy as np

        def calculate_var_m1(eepe_k_values):
            """Computes the variance of EEPE based on Method 1."""
            return np.var(eepe_k_values)
        ```

4.  **`calculate_conv_adj(m_val)`**
    *   **Purpose:** Computes the convergence adjustment factor $\text{convAdj}(m)$ for Method 1.
    *   **Parameters:**
        *   `m_val`: The number of Monte Carlo runs ($m$).
    *   **Returns:** The calculated convergence adjustment factor.
    *   **Mathematical Concept:**
        $$ \text{convAdj}(m) = \frac{t_{m-1, 0.975}}{\sqrt{m}} $$
        *(Note: The implementation uses a lookup table for specific $m$ values and approximates with $1.96 / \sqrt{m}$ for others.)*
    *   **Code Integration:**
        ```python
        import math

        def calculate_conv_adj(m_val):
            """Computes the convergence adjustment factor for Method 1."""
            if m_val <= 1:
                raise ValueError("m_val must be greater than 1")
            t_quantile = {
                2: 12.706,
                50: 2.009,
                100: 1.984,
                1000: 1.962
            }
            if m_val in t_quantile:
                adj_factor = t_quantile[m_val] / math.sqrt(m_val)
            else:
                 adj_factor = 1.96 / math.sqrt(m_val)
            return adj_factor
        ```

5.  **`calculate_error_m1(var_m1, conv_adj_val, phi_inv_0_975)`**
    *   **Purpose:** Computes the final Monte Carlo error for Method 1, $\text{error}_{m1}(\text{EEPE})$.
    *   **Parameters:**
        *   `var_m1`: Variance of EEPE from Method 1.
        *   `conv_adj_val`: Convergence adjustment factor.
        *   `phi_inv_0_975`: The $\Phi^{-1}(0.975)$ constant (1.96).
    *   **Returns:** The calculated Monte Carlo error for Method 1.
    *   **Mathematical Concept:**
        $$ \text{error}_{m1}(\text{EEPE}) = \sqrt{\text{var}_{m1}(\text{EEPE})} \times \text{convAdj}(m) \times \Phi^{-1}(0.975) $$
    *   **Code Integration:**
        ```python
        def calculate_error_m1(var_m1, conv_adj_val, phi_inv_0_975):
            """Computes the final Monte Carlo error for Method 1."""
            error_m1 = (var_m1**0.5) * conv_adj_val * phi_inv_0_975
            return error_m1
        ```

6.  **`calculate_var_m2(dj_values)`**
    *   **Purpose:** Computes the variance of $D_j$ values based on Method 2.
    *   **Parameters:**
        *   `dj_values`: A NumPy array of synthetic $D_j$ values.
    *   **Returns:** The calculated variance ($\text{var}_{m2}(\text{EEPE})$).
    *   **Mathematical Concept:**
        $$ \text{var}_{m2}(\text{EEPE}) = \frac{1}{N} \sum_{j=1}^{N} (D_j - \bar{D})^2 $$
    *   **Code Integration:**
        ```python
        def calculate_var_m2(dj_values):
            """Computes the variance of EEPE based on Method 2."""
            n = len(dj_values)
            if n <= 1:
                return 0.0
            mean = sum(dj_values) / n
            variance = sum([(x - mean) ** 2 for x in dj_values]) / n
            return variance
        ```

7.  **`calculate_error_m2(var_m2, phi_inv_0_975)`**
    *   **Purpose:** Computes the final Monte Carlo error for Method 2, $\text{error}_{m2}(\text{EEPE})$.
    *   **Parameters:**
        *   `var_m2`: Variance of $D_j$ values from Method 2.
        *   `phi_inv_0_975`: The $\Phi^{-1}(0.975)$ constant (1.96).
    *   **Returns:** The calculated Monte Carlo error for Method 2.
    *   **Mathematical Concept:**
        $$ \text{error}_{m2}(\text{EEPE}) = \sqrt{\text{var}_{m2}(\text{EEPE})} \times \Phi^{-1}(0.975) $$
    *   **Code Integration:**
        ```python
        def calculate_error_m2(var_m2, phi_inv_0_975):
            """Computes the final Monte Carlo error for Method 2."""
            error_m2 = phi_inv_0_975 * (var_m2**0.5)
            return error_m2
        ```

**Plotting Functions (to be adapted for Streamlit):**
These functions will generate `matplotlib` figures, which will then be displayed using `st.pyplot()`. `plt.show()` calls will be removed from the original functions.

1.  **`plot_method1_error(m_values, errors_m1)`**
    *   **Purpose:** Generates a line plot showing $\text{error}_{m1}(\text{EEPE})$ as a function of $m$.
    *   **Parameters:**
        *   `m_values`: A list or array of $m$ values for the x-axis.
        *   `errors_m1`: A list or array of corresponding $\text{error}_{m1}(\text{EEPE})$ values for the y-axis.
    *   **Code Integration (adapted for Streamlit):**
        ```python
        import matplotlib.pyplot as plt
        import numpy as np
        # In Streamlit, this function would return a figure object
        def plot_method1_error(m_values, errors_m1):
            """Generates a line plot showing error_m1(EEPE) as a function of $m$ ."""
            fig, ax = plt.subplots() # Create a figure and axes
            ax.plot(m_values, errors_m1)
            ax.set_xlabel("Number of MC Runs ($m$)")
            ax.set_ylabel("Calculated $\text{error}_{m1}(\text{EEPE})$")
            ax.set_title("Method 1: EEPE Monte Carlo Error vs. Number of MC Runs ($m$)")
            return fig # Return the figure
        ```

2.  **`plot_method2_error(N_values, errors_m2)`**
    *   **Purpose:** Generates a line plot showing $\text{error}_{m2}(\text{EEPE})$ as a function of $N$.
    *   **Parameters:**
        *   `N_values`: A list or array of $N$ values for the x-axis.
        *   `errors_m2`: A list or array of corresponding $\text{error}_{m2}(\text{EEPE})$ values for the y-axis.
    *   **Code Integration (adapted for Streamlit):**
        ```python
        import matplotlib.pyplot as plt
        import numpy as np
        # In Streamlit, this function would return a figure object
        def plot_method2_error(N_values, errors_m2):
            """Generates a line plot showing error_m2 as a function of N."""
            fig, ax = plt.subplots() # Create a figure and axes
            ax.plot(N_values, errors_m2)
            ax.set_xlabel("N")
            ax.set_ylabel("$\text{error}_{m2}(\text{EEPE})$")
            ax.set_title("Method 2: EEPE Monte Carlo Error vs. Number of Scenarios ($N$)")
            ax.grid(True)
            return fig # Return the figure
        ```

3.  **`plot_comparison_error(error_m1, error_m2)`**
    *   **Purpose:** Generates a bar chart comparing $\text{error}_{m1}(\text{EEPE})$ and $\text{error}_{m2}(\text{EEPE})$.
    *   **Parameters:**
        *   `error_m1`: The calculated $\text{error}_{m1}(\text{EEPE})$ for the current `m_runs`.
        *   `error_m2`: The calculated $\text{error}_{m2}(\text{EEPE})$ for the current `N_scenarios`.
    *   **Code Integration (adapted for Streamlit):**
        ```python
        import matplotlib.pyplot as plt
        # In Streamlit, this function would return a figure object
        def plot_comparison_error(error_m1, error_m2):
            """Generates a bar chart comparing error_m1 and error_m2."""
            fig, ax = plt.subplots() # Create a figure and axes
            ax.bar(['Method 1', 'Method 2'], [error_m1, error_m2])
            ax.set_title('Comparison of EEPE MC Error (Method 1 vs. Method 2)')
            ax.set_xlabel('Method')
            ax.set_ylabel('Calculated EEPE MC Error')
            ax.set_xticks(['Method 1', 'Method 2'])
            return fig # Return the figure
        ```

4.  **`plot_conv_adj_impact(m_values, conv_adj_values)`**
    *   **Purpose:** Generates a line plot showing $\text{convAdj}(m)$ as a function of $m$.
    *   **Parameters:**
        *   `m_values`: A list or array of $m$ values for the x-axis.
        *   `conv_adj_values`: A list or array of corresponding $\text{convAdj}(m)$ values for the y-axis.
    *   **Code Integration (adapted for Streamlit):**
        ```python
        import matplotlib.pyplot as plt
        import numpy as np
        # In Streamlit, this function would return a figure object
        def plot_conv_adj_impact(m_values, conv_adj_values):
            """Generates a line plot showing convAdj(m) as a function of m."""
            fig, ax = plt.subplots() # Create a figure and axes
            ax.plot(m_values, conv_adj_values)
            ax.set_xlabel('Number of MC Runs (m)')
            ax.set_ylabel('Convergence Adjustment Factor (convAdj(m))')
            ax.set_title('Impact of m on Convergence Adjustment Factor')
            ax.grid(True)
            return fig # Return the figure
        ```

**Streamlit Application Logic Flow (`update_display` concept):**
The `update_display` function in the notebook is a conceptual placeholder for how interactivity would work. In Streamlit, the entire script re-runs when a widget's value changes. The application logic will be structured as follows:

1.  **Import Streamlit and all necessary libraries.**
2.  **Define global constants and all utility/calculation functions** at the top of the script.
3.  **Set up the Streamlit UI components:**
    *   Title and overview markdown.
    *   Sidebar with input widgets (method selection, sliders for $m$, $N$, synthetic data mean/volatility, plot ranges).
4.  **Retrieve current values from widgets.**
5.  **Conditional Logic for Method 1 vs. Method 2:**
    *   If "Method 1" is selected:
        *   Generate synthetic $\text{EEPE}^k$ data using `generate_synthetic_eepe_k_data` with `m_runs`, `synthetic_mean`, `synthetic_volatility`.
        *   Calculate `var_m1` using `calculate_var_m1`.
        *   Calculate `conv_adj` using `calculate_conv_adj`.
        *   Calculate `error_m1` using `calculate_error_m1`.
        *   Display `error_m1`.
        *   Generate arrays for `m_values` and `errors_m1_plot` for the convergence plot (e.g., using `np.arange` up to `conv_adj_plot_max_m`).
        *   Call `plot_method1_error` and `plot_conv_adj_impact`, displaying the figures with `st.pyplot()`.
    *   If "Method 2" is selected:
        *   Generate synthetic $D_j$ data using `generate_synthetic_dj_data` with `N_scenarios`, `synthetic_mean`, `synthetic_volatility`.
        *   Calculate `var_m2` using `calculate_var_m2`.
        *   Calculate `error_m2` using `calculate_error_m2`.
        *   Display `error_m2`.
        *   Generate arrays for `N_values` and `errors_m2_plot` for the convergence plot (e.g., using `np.arange` up to `N_plot_max_N`).
        *   Call `plot_method2_error`, displaying the figure with `st.pyplot()`.
6.  **Comparison Plot (Always Visible):**
    *   Calculate `error_m1` and `error_m2` based on the *current* `m_runs` and `N_scenarios` (regardless of the selected method for primary display).
    *   Call `plot_comparison_error`, displaying the figure with `st.pyplot()`. This plot allows simultaneous comparison of single calculated points for both methods.
