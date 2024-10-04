import streamlit as st
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt


# Cache the file reading for performance optimization
@st.cache
def read_file(uploaded_file):
    """
    Read a CSV or Excel file and return a DataFrame.

    Args:
        uploaded_file: The uploaded file in CSV or Excel format.

    Returns:
        A pandas DataFrame.
    """
    if uploaded_file.name.endswith('.csv'):
        return pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('.xlsx'):
        return pd.read_excel(uploaded_file)
    return None


def validate_data(data):
    """
    Validate the data for analysis.

    Args:
        data: The numerical data to be validated.

    Returns:
        A tuple (bool, str): Whether the data is valid and an error message if not.
    """
    if len(data) < 2:
        return False, "Not enough data points for analysis."
    return True, None


def calculate_confidence_intervals(data, confidence_levels=[0.90, 0.95, 0.99]):
    """
    Calculate confidence intervals based on z-scores for the given data.

    Args:
        data (array-like): The numerical data to calculate the confidence intervals.
        confidence_levels (list): A list of confidence levels to calculate.

    Returns:
        tuple: Mean of the data and a dictionary of confidence intervals for each confidence level.
    """
    mean = np.mean(data)
    std_dev = np.std(data, ddof=1)
    n = len(data)
    confidence_intervals = {}

    if n <= 1:
        return mean, {}

    for confidence in confidence_levels:
        z_value = stats.norm.ppf((1 + confidence) / 2)
        margin_of_error = z_value * (std_dev / np.sqrt(n))
        confidence_intervals[confidence] = (mean - margin_of_error, mean + margin_of_error)

    return mean, confidence_intervals


def calculate_confidence_interval_se(data, se_value):
    """
    Calculate confidence intervals based on the number of standard errors provided by the user.

    Args:
        data (array-like): The numerical data to calculate the confidence intervals.
        se_value (float): The number of standard errors to use for margin of error calculation.

    Returns:
        tuple: The lower and upper bounds of the confidence interval.
    """
    mean = np.mean(data)
    std_dev = np.std(data, ddof=1)
    n = len(data)

    if n <= 1:
        return None

    standard_error = std_dev / np.sqrt(n)
    margin_of_error = se_value * standard_error
    return mean - margin_of_error, mean + margin_of_error


def plot_distribution(data, column_name):
    """
    Plot a histogram of the data for the selected column.

    Args:
        data (pd.Series): The numerical data to plot.
        column_name (str): The name of the column being plotted.
    """
    plt.figure(figsize=(8, 6))
    plt.hist(data, bins=20, edgecolor='k', alpha=0.7)
    plt.title(f"Frequency Distribution of {column_name}")
    plt.xlabel(column_name)
    plt.ylabel("Frequency")
    st.pyplot(plt)


def main():
    """
    Main function to run the Streamlit app for confidence interval calculation.
    """
    st.title("Confidence Interval Calculator")

    # File upload section
    uploaded_file = st.file_uploader("Upload your CSV or Excel file", type=["csv", "xlsx"])

    if uploaded_file:
        try:
            # Read the file using caching to optimize performance
            df = read_file(uploaded_file)

            if df is None or df.empty:
                st.error("The uploaded file is empty or invalid.")
                return

            # Display the uploaded dataframe
            st.write("Here is a preview of your uploaded file:")
            st.dataframe(df)

            # Select the column for analysis
            numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()

            if numeric_columns:
                selected_column = st.selectbox("Select the column with numerical data", numeric_columns)

                if selected_column:
                    # Extract the data from the selected column
                    data = df[selected_column].dropna()

                    # Validate the data
                    is_valid, error_message = validate_data(data)
                    if not is_valid:
                        st.error(error_message)
                        return

                    # Plot frequency distribution of the selected column
                    st.subheader(f"Frequency Distribution of {selected_column}")
                    plot_distribution(data, selected_column)

                    # Allow user to input custom confidence levels
                    st.subheader("Confidence Intervals based on Z-scores")
                    confidence_input = st.text_input(
                        "Enter confidence levels (comma-separated, e.g., 0.90, 0.95, 0.99)", "0.90, 0.95, 0.99")
                    try:
                        confidence_levels = [float(x) for x in confidence_input.split(',')]
                    except ValueError:
                        st.error("Invalid confidence levels. Please enter numbers separated by commas.")
                        return

                    # Calculate confidence intervals
                    mean, confidence_intervals = calculate_confidence_intervals(data, confidence_levels)

                    # Display results
                    st.write(f"Sample Mean: {mean:.4f}")
                    for confidence, interval in confidence_intervals.items():
                        st.write(
                            f"{int(confidence * 100)}% Confidence Interval: ({interval[0]:.4f}, {interval[1]:.4f})")

                    # Option for Standard Error based confidence interval calculation
                    st.subheader("Confidence Interval based on Standard Errors")
                    se_value = st.number_input("Enter the number of standard errors (e.g., 1.96 for 95%)",
                                               min_value=0.0, value=1.96, step=0.01)
                    ci_se = calculate_confidence_interval_se(data, se_value)

                    if ci_se:
                        st.write(
                            f"Confidence Interval using {se_value} Standard Errors: ({ci_se[0]:.4f}, {ci_se[1]:.4f})")
                    else:
                        st.error("Not enough data to calculate the confidence interval using standard errors.")
            else:
                st.error("No numerical columns found in the uploaded file.")
        except Exception as e:
            st.error(f"Error reading file: {e}")
    else:
        st.info("Please upload a CSV or Excel file to proceed.")


# Run the app
if __name__ == "__main__":
    main()
