
# Technical Specification for EEPE Monte Carlo Error Calculator Jupyter Notebook

This document specifies the design and functional requirements for a Jupyter Notebook that demonstrates and compares two methodologies for estimating the Monte Carlo (MC) error of Expected Positive Exposure (EEPE).

## 1. Notebook Overview

This Jupyter Notebook provides an interactive environment for users to understand and compare Method 1 and Method 2 for calculating the Monte Carlo error of Expected Positive Exposure (EEPE). Through interactive parameters and dynamic visualizations, learners can explore the impact of simulation settings on error estimates and convergence.

### Learning Goals

*   Understand and implement Method 1 and Method 2 for estimating EEPE Monte Carlo error.
*   Aggregate the theoretical results and methodologies from the provided documentation.

### Expected Outcomes

Upon completing this notebook, users will be able to:

*   **Comprehend the Theoretical Basis:** Gain a solid understanding of the mathematical foundations behind Method 1 and Method 2 for EEPE error estimation.
*   **Implement Methodologies:** Understand the algorithmic steps required to implement both error calculation methods using synthetic data.
*   **Analyze Parameter Impact:** Demonstrate how key simulation parameters, such as the number of MC runs ($m$) for Method 1 and the number of scenarios ($N$) for Method 2, directly influence the precision and convergence of EEPE error estimates.
*   **Compare Method Characteristics:** Identify the strengths and differences between Method 1 and Method 2, including the application of convergence adjustments.
*   **Utilize Interactive Tools:** Effectively use interactive Jupyter widgets to explore various scenarios and visualize results dynamically.

## 2. Mathematical and Theoretical Foundations

This section will lay out the core mathematical definitions and formulas from the provided Annex document, presented within the Jupyter Notebook as Markdown cells.

### 2.1. Introduction to EEPE Monte Carlo Error

**Markdown Cell:**
The Monte Carlo (MC) error on the Estimated Expected Positive Exposure (EEPE) is defined as half the length of the 95% two-sided confidence interval centered around the sample estimated EEPE. This notebook explores two distinct methodologies for estimating this error: Method 1 and Method 2. Both methods assume that EEPE values are obtained from pseudo Monte Carlo simulations using random number generators.

A "MC run" refers to a pseudo Monte Carlo simulation conducted with $N$ scenarios using one particular set of random numbers.

### 2.2. Common Assumptions and Definitions

**Markdown Cell:**
For the purpose of estimating the Monte Carlo error, it is typically assumed that EEPE values, or the underlying aggregated exposure values, follow a normal distribution. This assumption is crucial for interpreting the error as half the length of a 95% confidence interval.
The inverse cumulative function of a standard normal distribution, $\Phi^{-1}(x)$, is used to determine the confidence interval. Specifically, $\Phi^{-1}(0.975)$ corresponds to the 97.5th percentile of the standard normal distribution, which is approximately $1.96$.
$$ \Phi^{-1}(0.975) \approx 1.96 $$

### 2.3. Method 1: Estimation via Multiple MC Runs

**Markdown Cell:**
Method 1 estimates the MC error on EEPE by utilizing a set of multiple MC runs. Let $m$ denote the number of such MC runs, where each run $k$ (for $k=1, \dots, m$) provides an estimate of EEPE, denoted as $\text{EEPE}^k$. These different $\text{EEPE}^k$ values are obtained by running the MC simulation with different random numbers (e.g., by using different seeds).

**Variance Calculation for Method 1:**
The variance of EEPE using Method 1, denoted as $\text{var}_{m1}(\text{EEPE})$, is calculated based on the sample variance of the $m$ EEPE estimates:

$$ \text{var}_{m1}(\text{EEPE}) := \frac{1}{m-1}\sum_{k=1}^{m}\left(\text{EEPE}^k - \frac{1}{m}\sum_{l=1}^{m}\text{EEPE}^l\right)^2 $$

Here, $\text{EEPE}^k$ denotes the estimation of EEPE using the $k$-th run of the MC run set.

**Convergence Adjustment Factor ($\text{convAdj}(m)$):**
For small values of $m$ (e.g., $m < 50$), $\text{var}_{m1}(\text{EEPE})$ may not have properly converged to the true variance of EEPE, $\text{var}(\text{EEPE})$. To address this, a convergence adjustment factor, $\text{convAdj}(m)$, is introduced. This factor ensures that the confidence interval remains statistically sound.

The parameter $\text{convAdj}(m)$ is chosen such that:
$$ P\left(\sqrt{\text{var}(\text{EEPE})} < \text{convAdj}(m) \sqrt{\text{var}_{m1}(\text{EEPE})}\right) = 95\% $$
Assuming $\text{EEPE}$ follows a normal distribution, $\text{convAdj}(m)$ can be calculated as:
$$ \text{convAdj}(m) = \sqrt{\frac{m-1}{q(m-1; 97.5\%)}} $$
where $q(m-1; 97.5\%)$ is the 97.5th percentile of a standard chi-squared distribution with $m-1$ degrees of freedom, denoted as $\chi^2_{m-1}$. That is, $P(Z \le q(m-1; 97.5\%)) = 97.5\%$ for $Z \sim \chi^2_{m-1}$.

**MC Error Formula for Method 1:**
The Monte Carlo error on EEPE using Method 1 is defined as:
$$ \text{error}_{m1}(\text{EEPE}) := \Phi^{-1}(0.975) \cdot \text{convAdj}(m) \cdot \sqrt{\text{var}_{m1}(\text{EEPE})} $$
Given $\Phi^{-1}(0.975) \approx 1.96$, the formula simplifies to:
$$ \text{error}_{m1}(\text{EEPE}) \approx 1.96 \cdot \text{convAdj}(m) \cdot \sqrt{\text{var}_{m1}(\text{EEPE})} $$

### 2.4. Method 2: Estimation via a Single MC Run

**Markdown Cell:**
Method 2 estimates the MC error on EEPE based on a single MC run with $N$ simulations (scenarios). Unlike Method 1, it does not require multiple full MC runs.

**Definition of $D_j$:**
For each scenario $j$ (from $1$ to $N$), an aggregated exposure value $D_j$ is defined. This $D_j$ represents the weighted sum of netting set exposures across relevant time points, $t_k$, for scenario $j$.
$$ D_j := \sum_{u=1}^{p-1}(v_u - v_{u-1})E_j(S_u) + (t_{1y} - v_{p-1})E_j(S_p) $$
where:
*   $E_j(S_u)$ stands for the netting set exposure level at effective reference date $S_u$ for scenario $j$.
*   $v_u$ are "application period dates" representing time intervals over which $\text{EEPE}(S_u)$ is applied.
By definition, the EEPE can be expressed as the average of $D_j$ values:
$$ \text{EEPE} = \frac{1}{N}\sum_{j=1}^{N} D_j $$

**Variance Calculation for Method 2:**
The variance of EEPE using Method 2, denoted as $\text{var}_{m2}(\text{EEPE})$, is derived from the variance of the $D_j$ values:
$$ \text{var}_{m2}(\text{EEPE}) = \frac{1}{N}\text{var}(D) = \frac{1}{N(N-1)}\sum_{j=1}^{N}(D_j - \text{EEPE})^2 $$

**MC Error Formula for Method 2:**
The Monte Carlo error on EEPE using Method 2 is defined as:
$$ \text{error}_{m2}(\text{EEPE}) := \Phi^{-1}(0.975) \sqrt{\text{var}_{m2}(\text{EEPE})} $$
Given $\Phi^{-1}(0.975) \approx 1.96$, the formula simplifies to:
$$ \text{error}_{m2}(\text{EEPE}) \approx 1.96 \cdot \sqrt{\text{var}_{m2}(\text{EEPE})} $$

**Absence of Convergence Adjustment for Method 2:**
No explicit convergence adjustment is needed for Method 2 for usual values of $N$. This is because for large $N$, the implicit convergence adjustment factor for $N$ is very close to 1 (e.g., $\text{convAdj}(500) \approx 1.067$ and $\text{convAdj}(1000) \approx 1.046$, indicating diminishing impact with increasing $N$).

### 2.5. Aggregation Across Netting Sets (Brief Note)

**Markdown Cell:**
While this notebook focuses on calculating the Monte Carlo error for a single netting set for simplicity, the document briefly mentions methods for aggregating errors across multiple netting sets or "silos." In general, for Method 1, aggregation would involve summing the EEPE estimates for all netting sets *before* calculating the variance. For Method 2, the $D_j$ terms would be summed across netting sets *before* calculating their variance. If exposures are estimated through separate "silos," the total portfolio error can be derived by summing the squared errors from each silo:
$$ \text{error}_{m1}(\text{EEPE of total portfolio}) = \sqrt{\sum_{i=1}^{S} \left(\text{error}_{m1}(\text{EEPE}_{\text{N of silo}_i})\right)^2} $$
where $S$ is the total number of silos.

## 3. Code Requirements

This section outlines the structure, libraries, functions, and visualizations required for the interactive Jupyter Notebook.

### 3.1. Logical Flow of the Notebook

The notebook will follow a clear logical progression, guiding the user through the setup, data generation, method implementations, and interactive analysis.

1.  **Setup and Imports:**
    *   Import necessary Python libraries.
    *   Define global constants (e.g., $\Phi^{-1}(0.975) \approx 1.96$).
2.  **Helper Functions Definition:**
    *   Define functions for synthetic data generation specific to each method.
    *   Define functions for calculating variance, convergence adjustment, and final error for both methods.
3.  **Interactive Controls Setup:**
    *   Set up `ipywidgets` for user interaction (sliders, dropdown).
    *   Define default parameter values for synthetic data generation and simulation runs.
4.  **Interactive Display Logic:**
    *   Define an `interact` function or similar callback that will update calculations and plots based on widget changes. This function will:
        *   Clear previous outputs (if any).
        *   Determine which method/view is selected by the user.
        *   Generate synthetic data based on user-defined parameters.
        *   Perform calculations for the selected method(s).
        *   Generate and display the appropriate plots and numerical results.
5.  **Initial Display:**
    *   Call the interactive display function with initial parameter values to show the default state of the analysis.

### 3.2. Expected Libraries

The following open-source Python libraries from PyPI are expected to be used:

*   **`numpy`**: For efficient numerical operations, array creation, and statistical functions (e.g., `mean`, `std`, `sqrt`).
*   **`scipy.stats`**: For statistical distributions and functions, specifically:
    *   `norm.ppf()`: For $\Phi^{-1}(0.975)$.
    *   `chi2.ppf()`: For calculating $q(m-1; 97.5\%)$ required for `convAdj(m)`.
*   **`matplotlib.pyplot`**: For creating static and dynamic plots.
*   **`ipywidgets`**: For creating interactive user interface elements such as sliders, dropdowns, and interactive output displays.

### 3.3. Input/Output Expectations

**Inputs (via `ipywidgets`):**

*   **Method Selection:**
    *   **Type:** Dropdown/Radio buttons.
    *   **Options:** "Method 1: Multiple MC Runs", "Method 2: Single MC Run", "Comparison", "ConvAdj(m) Impact".
    *   **Inline Help:** "Select the Monte Carlo error estimation method to explore."
*   **Method 1 Parameters:** (Visible only when "Method 1" or "Comparison" is selected)
    *   **`m_runs`:** Slider for the number of MC runs ($m$).
        *   **Range:** e.g., 2 to 200 (with step 1).
        *   **Default:** e.g., 50.
        *   **Inline Help:** "Number of independent Monte Carlo runs to estimate EEPE (m)."
*   **Method 2 Parameters:** (Visible only when "Method 2" or "Comparison" is selected)
    *   **`N_scenarios`:** Slider for the number of scenarios ($N$) within a single MC run.
        *   **Range:** e.g., 1000 to 20000 (with step 100).
        *   **Default:** e.g., 5000.
        *   **Inline Help:** "Number of simulations/scenarios within a single Monte Carlo run (N)."
*   **Synthetic Data Properties:** (Visible for all methods)
    *   **`synthetic_mean`:** Slider for the mean of the synthetic EEPE/aggregated exposure ($D_j$) data.
        *   **Range:** e.g., 50 to 200.
        *   **Default:** e.g., 100.
        *   **Inline Help:** "Mean value for the synthetic EEPE or aggregated exposure (Dj) data."
    *   **`synthetic_volatility`:** Slider for the volatility (standard deviation) of the synthetic EEPE/aggregated exposure ($D_j$) data.
        *   **Range:** e.g., 5 to 50.
        *   **Default:** e.g., 20.
        *   **Inline Help:** "Volatility (standard deviation) for the synthetic EEPE or aggregated exposure (Dj) data."
*   **ConvAdj Plot Range:** (Visible only when "ConvAdj(m) Impact" is selected)
    *   **`conv_adj_plot_max_m`:** Slider for the maximum $m$ to plot $\text{convAdj}(m)$.
        *   **Range:** e.g., 2 to 100.
        *   **Default:** e.g., 50.
        *   **Inline Help:** "Maximum number of MC runs (m) to display the convergence adjustment factor."

**Outputs:**

*   **Numerical Results:**
    *   Calculated $\text{error}_{m1}(\text{EEPE})$ and $\text{convAdj}(m)$ (when Method 1 is selected).
    *   Calculated $\text{error}_{m2}(\text{EEPE})$ (when Method 2 is selected).
    *   Summary of current parameter values.
*   **Visualizations:** As detailed in section 3.5.
*   **Narrative Cells:** Brief explanations (what and why) accompanying code sections and outputs.

### 3.4. Algorithms and Functions (Conceptual, No Code)

The notebook will define the following conceptual functions:

1.  **`generate_synthetic_eepe_k_data(m_runs, mean, std_dev)`:**
    *   **Purpose:** To generate `m_runs` synthetic EEPE values, each representing $\text{EEPE}^k$ from an independent MC run.
    *   **Input:** Number of MC runs (`m_runs`), desired mean, and standard deviation for the synthetic data.
    *   **Output:** A NumPy array of `m_runs` floating-point numbers, representing synthetic $\text{EEPE}^k$ values.

2.  **`generate_synthetic_dj_data(N_scenarios, mean, std_dev)`:**
    *   **Purpose:** To generate `N_scenarios` synthetic $D_j$ values, representing the aggregated exposure for each scenario $j$ in a single MC run.
    *   **Input:** Number of scenarios (`N_scenarios`), desired mean, and standard deviation for the synthetic data.
    *   **Output:** A NumPy array of `N_scenarios` floating-point numbers, representing synthetic $D_j$ values.

3.  **`calculate_var_m1(eepe_k_values)`:**
    *   **Purpose:** Computes the variance of EEPE based on Method 1.
    *   **Input:** Array of synthetic $\text{EEPE}^k$ values.
    *   **Output:** Single float, $\text{var}_{m1}(\text{EEPE})$.

4.  **`calculate_conv_adj(m_val)`:**
    *   **Purpose:** Computes the convergence adjustment factor for Method 1.
    *   **Input:** Integer `m_val` (number of MC runs).
    *   **Output:** Single float, $\text{convAdj}(m)$. Utilizes `scipy.stats.chi2.ppf` for the chi-squared percentile.

5.  **`calculate_error_m1(var_m1, conv_adj_val, phi_inv_0_975)`:**
    *   **Purpose:** Computes the final Monte Carlo error for Method 1.
    *   **Input:** $\text{var}_{m1}$, $\text{convAdj}(m)$, and the constant $\Phi^{-1}(0.975)$.
    *   **Output:** Single float, $\text{error}_{m1}(\text{EEPE})$.

6.  **`calculate_var_m2(dj_values)`:**
    *   **Purpose:** Computes the variance of EEPE based on Method 2.
    *   **Input:** Array of synthetic $D_j$ values.
    *   **Output:** Single float, $\text{var}_{m2}(\text{EEPE})$.

7.  **`calculate_error_m2(var_m2, phi_inv_0_975)`:**
    *   **Purpose:** Computes the final Monte Carlo error for Method 2.
    *   **Input:** $\text{var}_{m2}$ and the constant $\Phi^{-1}(0.975)$.
    *   **Output:** Single float, $\text{error}_{m2}(\text{EEPE})$.

8.  **`plot_method1_error(m_values, errors_m1)`:**
    *   **Purpose:** Generates a line plot showing $\text{error}_{m1}(\text{EEPE})$ as a function of $m$.
    *   **Input:** Arrays of $m$ values and corresponding $\text{error}_{m1}(\text{EEPE})$ values.

9.  **`plot_method2_error(N_values, errors_m2)`:**
    *   **Purpose:** Generates a line plot showing $\text{error}_{m2}(\text{EEPE})$ as a function of $N$.
    *   **Input:** Arrays of $N$ values and corresponding $\text{error}_{m2}(\text{EEPE})$ values.

10. **`plot_comparison_error(error_m1, error_m2)`:**
    *   **Purpose:** Generates a bar chart comparing the calculated $\text{error}_{m1}(\text{EEPE})$ and $\text{error}_{m2}(\text{EEPE})$ for the currently selected $m$ and $N$.
    *   **Input:** Single float values for $\text{error}_{m1}$ and $\text{error}_{m2}$.

11. **`plot_conv_adj_impact(m_values, conv_adj_values)`:**
    *   **Purpose:** Generates a line plot showing $\text{convAdj}(m)$ as a function of $m$.
    *   **Input:** Arrays of $m$ values and corresponding $\text{convAdj}(m)$ values.

12. **`update_display(selected_method, m_runs, N_scenarios, synthetic_mean, synthetic_volatility, conv_adj_plot_max_m)`:**
    *   **Purpose:** The main callback function for `ipywidgets.interact`. It orchestrates data generation, calculations, and plot updates based on user inputs.
    *   **Input:** All widget values.
    *   **Output:** Displays numerical results and plots dynamically within the notebook.

### 3.5. Visualization Requirements

The notebook will generate dynamic plots based on user interactions:

1.  **Plot 1: Method 1 Error vs. MC Runs ($m$)**
    *   **Type:** Line plot.
    *   **X-axis:** "Number of MC Runs ($m$)"
    *   **Y-axis:** "Calculated $\text{error}_{m1}(\text{EEPE})$"
    *   **Title:** "Method 1: EEPE Monte Carlo Error vs. Number of MC Runs ($m$)"
    *   **Behavior:** Updates dynamically as the `m_runs` slider is adjusted. A range of $m$ values (e.g., from a small minimum up to the slider's current value) will be used to show the trend.

2.  **Plot 2: Method 2 Error vs. Number of Scenarios ($N$)**
    *   **Type:** Line plot.
    *   **X-axis:** "Number of Scenarios ($N$)"
    *   **Y-axis:** "Calculated $\text{error}_{m2}(\text{EEPE})$"
    *   **Title:** "Method 2: EEPE Monte Carlo Error vs. Number of Scenarios ($N$)"
    *   **Behavior:** Updates dynamically as the `N_scenarios` slider is adjusted. A range of $N$ values (e.g., from a small minimum up to the slider's current value) will be used to show the trend.

3.  **Plot 3: Comparison of Error Magnitudes**
    *   **Type:** Bar chart.
    *   **X-axis:** "Method" (labels: "Method 1", "Method 2")
    *   **Y-axis:** "Calculated EEPE MC Error"
    *   **Title:** "Comparison of EEPE MC Error (Method 1 vs. Method 2)"
    *   **Behavior:** Displays the current calculated $\text{error}_{m1}(\text{EEPE})$ for the selected $m$ and $\text{error}_{m2}(\text{EEPE})$ for the selected $N$. This visualization helps users directly compare the magnitude of errors derived from each method given their respective current parameter settings.

4.  **Plot 4: $\text{convAdj}(m)$ Impact**
    *   **Type:** Line plot.
    *   **X-axis:** "Number of MC Runs ($m$)"
    *   **Y-axis:** "Convergence Adjustment Factor ($\text{convAdj}(m)$)"
    *   **Title:** "Impact of $m$ on Convergence Adjustment Factor"
    *   **Behavior:** Shows how $\text{convAdj}(m)$ decreases as $m$ increases, demonstrating its importance for small $m$ and its convergence to 1 for larger $m$. The plot range for $m$ will be controllable by the `conv_adj_plot_max_m` slider.

## 4. Additional Notes or Instructions

### 4.1. Assumptions

*   **Normal Distribution:** Both error estimation methods fundamentally rely on the assumption that the EEPE, or the underlying aggregated exposure values ($D_j$), follows a normal distribution.
*   **Synthetic Data Representativeness:** The synthetic data generated for this demonstration is intended to illustrate the mechanics of the formulas. It is assumed that this simulated data sufficiently approximates real-world EEPE/exposure distributions for pedagogical purposes.
*   **Method 1 EEPE^k:** For Method 1, each $\text{EEPE}^k$ value is treated as an independent outcome from a full MC run, without explicitly simulating the $N$ scenarios within each of those $m$ runs.
*   **Method 2 $D_j$ Values:** For Method 2, the $D_j$ values are treated as independent outcomes representing the aggregated exposure for each scenario $j$, simplifying the complex derivation from individual exposures $E_j(t_k)$.

### 4.2. Constraints

*   **Open-Source Python Libraries:** Only libraries available on PyPI and explicitly mentioned in Section 3.2 are permitted.
*   **No Deployment Details:** This specification is strictly for the Jupyter Notebook content and functionality. It does not cover deployment, hosting, or integration with external platforms.
*   **No Python Code in Specification:** This document provides conceptual algorithms and function descriptions, not executable Python code.
*   **Narrative and Comments:** All major steps in the notebook's code and analysis will be accompanied by descriptive Markdown cells explaining "what" is happening and "why", along with inline code comments.
*   **LaTeX Formatting:** All mathematical content, especially formulas and equations, must adhere strictly to the specified LaTeX formatting rules: `$$...$$` for display equations and `$...$` for inline equations.

### 4.3. Customization and Exploration Instructions for Users

*   **Parameter Manipulation:** Users are strongly encouraged to actively interact with the sliders and dropdowns provided. Experimenting with different values for $m$, $N$, synthetic mean, and volatility will directly demonstrate their impact on the calculated errors and observed convergence patterns.
*   **Code Exploration:** Learners can inspect the Python code cells to understand how the synthetic data is generated and how each mathematical formula is translated into code.
*   **Theoretical Deep Dive:** Refer back to the "Mathematical and Theoretical Foundations" sections to reinforce the understanding of the formulas and the rationale behind each method.
*   **Further Enhancements (Self-Study):**
    *   Consider how more realistic synthetic data generation (e.g., correlated exposures, specific distributions) might affect the results.
    *   Explore how to implement the aggregation across netting sets (Section 2.5) if provided with hypothetical multi-netting set data.
    *   Investigate the impact of different confidence levels (e.g., 90% or 99%) on the error calculation.

