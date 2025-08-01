Here's a comprehensive `README.md` file for your Streamlit application lab project, formatted in Markdown.

---

# QuLab: ECB-Annex Monte Carlo Error Analysis

![QuLab Logo](https://www.quantuniversity.com/assets/img/logo5.jpg)

## Project Title and Description

This Streamlit application, named "QuLab: ECB-Annex Lab," provides an interactive platform for users to understand, implement, and compare two distinct methodologies (Method 1 and Method 2) for estimating the Monte Carlo (MC) error of Expected Positive Exposure (EEPE) in counterparty credit risk. The application allows users to manipulate key simulation parameters and observe their direct impact on error estimates and convergence behavior.

**The primary objectives of this lab project are:**

*   To enable users to understand and implement the calculations for $\text{error}_{m1}(\text{EEPE})$ and $\text{error}_{m2}(\text{EEPE})$.
*   To visualize the relationship between simulation parameters (number of MC runs $m$, number of scenarios $N$) and the calculated Monte Carlo errors.
*   To compare the error magnitudes derived from both Method 1 and Method 2.
*   To illustrate the impact of the convergence adjustment factor $\text{convAdj}(m)$ on Method 1's error.
*   To provide an intuitive, interactive experience for exploring the sensitivities of EEPE error estimation.

**Business Value:**
Understanding and accurately calculating Monte Carlo error in EEPE is critical for regulatory compliance and sound risk management in financial institutions. This application offers a hands-on tool to explore different methodologies and their sensitivities, enabling better model validation, risk assessment, and resource allocation for computationally intensive simulations.

## Features

*   **Interactive Parameter Control**: Adjust synthetic data mean, volatility, number of Monte Carlo runs (`m`), and number of scenarios (`N`) using intuitive sliders in the sidebar.
*   **Method 1 Error Estimation**:
    *   Calculates and displays $\text{error}_{m1}(\text{EEPE})$ based on multiple independent MC runs.
    *   Visualizes the convergence of $\text{error}_{m1}(\text{EEPE})$ as `m` increases.
    *   Illustrates the impact of the Student's t-distribution-based `convAdj(m)` factor.
*   **Method 2 Error Estimation**:
    *   Calculates and displays $\text{error}_{m2}(\text{EEPE})$ based on the variance of individual discounted positive exposures (`Dj`).
    *   Visualizes the convergence of $\text{error}_{m2}(\text{EEPE})$ as `N` (number of scenarios) increases.
*   **Comparative Analysis**:
    *   A dedicated "Comparison" page to directly contrast the calculated errors from Method 1 and Method 2 side-by-side using consistent input parameters.
    *   Bar chart visualization for easy comparison of error magnitudes.
*   **Synthetic Data Generation**: Utility functions to generate synthetic `EEPE^k` and `Dj` values for demonstration purposes.
*   **Clear Formula Presentation**: Mathematical formulas for error calculations are presented directly within the application for clarity.

## Getting Started

Follow these instructions to set up and run the application on your local machine.

### Prerequisites

Ensure you have Python 3.7+ installed. The application relies on the following Python libraries:

*   `streamlit`
*   `numpy`
*   `plotly`

### Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/quolab-ecb-annex-lab.git
    cd quolab-ecb-annex-lab
    ```
    *(Replace `your-username/quolab-ecb-annex-lab` with the actual repository URL)*

2.  **Create a virtual environment (recommended)**:
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the required libraries**:
    ```bash
    pip install -r requirements.txt
    ```
    If you don't have a `requirements.txt` file, you can create one with the following content:
    ```
    streamlit>=1.0.0
    numpy>=1.20.0
    plotly>=5.0.0
    ```
    Then run `pip install -r requirements.txt`.
    Alternatively, install them manually:
    ```bash
    pip install streamlit numpy plotly
    ```

## Usage

1.  **Run the Streamlit application**:
    From the root directory of the cloned repository (where `app.py` is located), execute:
    ```bash
    streamlit run app.py
    ```

2.  **Access the Application**:
    Your web browser should automatically open the application at `http://localhost:8501`. If not, navigate to this URL manually.

3.  **Navigate and Interact**:
    *   Use the sidebar on the left to navigate between "Method 1", "Method 2", and "Comparison" pages.
    *   On each page, adjust the parameters using the sliders in the sidebar to observe changes in the calculated errors and their convergence plots.
    *   The "Comparison" page allows you to set parameters for both methods simultaneously and see their relative performance.

## Project Structure

The project is organized into logical directories for maintainability:

```
quolab-ecb-annex-lab/
├── app.py                      # Main Streamlit application entry point and navigation.
├── application_pages/          # Directory containing logic for different application pages.
│   ├── __init__.py             # Makes application_pages a Python package.
│   ├── utils.py                # Contains core mathematical functions and synthetic data generation.
│   ├── page1.py                # Logic and UI for "Method 1" error estimation page.
│   ├── page2.py                # Logic and UI for "Method 2" error estimation page.
│   └── page3.py                # Logic and UI for "Comparison" page.
├── requirements.txt            # Lists all Python dependencies.
└── README.md                   # This README file.
```

### Key Files Breakdown:

*   `app.py`: Sets up the main page layout, sidebar navigation, and routes to different application pages. It also contains the overall project description and objectives.
*   `application_pages/utils.py`: This file is the computational backbone. It defines functions for:
    *   `generate_synthetic_eepe_k_data`: Creates synthetic data for Method 1.
    *   `generate_synthetic_dj_data`: Creates synthetic data for Method 2.
    *   `calculate_var_m1`, `calculate_conv_adj`, `calculate_error_m1`: Core calculations for Method 1.
    *   `calculate_var_m2`, `calculate_error_m2`: Core calculations for Method 2.
    *   `phi_inv_0_975`: A constant representing the 97.5th percentile of the standard normal distribution, used in error calculations.
*   `application_pages/page1.py`: Implements the UI and logic specific to Method 1, including parameter sliders, error calculation display, and convergence plots for `m` and the convergence adjustment factor.
*   `application_pages/page2.py`: Implements the UI and logic specific to Method 2, including parameter sliders, error calculation display, and convergence plots for `N`.
*   `application_pages/page3.py`: Implements the UI and logic for comparing both methods side-by-side, displaying calculated errors and a comparative bar chart.

## Technology Stack

*   **Python**: The core programming language for the entire application.
*   **Streamlit**: An open-source app framework for Machine Learning and Data Science teams. It's used to create the interactive web user interface.
*   **NumPy**: A fundamental package for numerical computing with Python, used extensively for array operations and synthetic data generation.
*   **Plotly**: A graphing library that makes interactive, publication-quality graphs. Used for all the data visualizations within the application.

## Contributing

This project is primarily for educational and lab purposes. However, if you have suggestions for improvements or find a bug, feel free to open an issue or submit a pull request.

1.  Fork the repository.
2.  Create your feature branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a Pull Request.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details (if you create one, otherwise state "MIT License" is implied for this example).

## Contact

For questions or inquiries, please contact the QuantUniversity team or the project maintainer.

QuantUniversity: [https://www.quantuniversity.com/](https://www.quantuniversity.com/)

---