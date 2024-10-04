# Confidence-Intervals
Streamlit local application to calculate confidence intervals and view frequency distributions!

This is a Streamlit-based web application that allows users to upload CSV or Excel files containing numerical data and calculate confidence intervals for the data. The application supports both Z-score-based confidence intervals and confidence intervals based on a user-defined number of standard errors.
![image](https://github.com/user-attachments/assets/cbf1505d-f222-4470-a258-cdffb8490d8b) ![image](https://github.com/user-attachments/assets/a30327a1-b194-4d99-9cdd-f26240e9025b)



## Features

- **File Upload**: Users can upload a CSV or Excel file containing their data.
- **Data Validation**: The application validates that the uploaded file contains enough numerical data for statistical analysis.
- **Confidence Interval Calculation**:
  - **Z-Score Based**: Allows users to calculate confidence intervals for different confidence levels (e.g., 90%, 95%, 99%).
  - **Standard Error Based**: Allows users to calculate confidence intervals based on a specified number of standard errors.
- **Data Visualization**: Displays a histogram of the data to visualize its frequency distribution.
- **Interactive Inputs**: Users can select the column for analysis, set custom confidence levels, and specify the number of standard errors.

## How to Run

1. **Install Dependencies**:
   Before running the app, you need to install the required dependencies. You can do this by running the following command:

   ```bash
   pip install streamlit pandas numpy scipy matplotlib
   ```

2. **Run the Application**:
   To run the application, use the following command:

   ```bash
   streamlit run app.py
   ```

   This will start a local server and open the application in your default web browser.

## How to Use

1. **Upload Data**:
   - Upload a CSV or Excel file containing numerical data.
   - The application will automatically display a preview of the uploaded data.

2. **Select Numerical Column**:
   - Choose the column with the numerical data you want to analyze.
   - The app will validate if the selected column has enough data points for analysis.

3. **Plot Frequency Distribution**:
   - A histogram showing the frequency distribution of the selected data column will be generated.

4. **Confidence Interval Calculation**:
   - **Z-Score Confidence Intervals**:
     - Enter a comma-separated list of confidence levels (e.g., 0.90, 0.95, 0.99).
     - The app will calculate and display confidence intervals for each specified level.
   - **Standard Error Confidence Intervals**:
     - Input the number of standard errors (e.g., 1.96 for a 95% confidence interval).
     - The app will calculate and display the confidence interval based on the number of standard errors.

## Example

After uploading a file and selecting a numerical column, you can input confidence levels or standard error values. The app will output the calculated sample mean and confidence intervals.

For example:

```
Sample Mean: 50.23
95% Confidence Interval: (45.12, 55.34)
```

## Project Structure

```plaintext
.
├── app.py            # Main application script
├── README.md         # Documentation file
└── requirements.txt  # List of dependencies
```

## Requirements

- **Python 3.7+**
- **Streamlit**
- **Pandas**
- **NumPy**
- **SciPy**
- **Matplotlib**

You can install all the dependencies with:

```bash
pip install -r requirements.txt
```
