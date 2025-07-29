# Bank Stock Financial Analysis
Project Overview

This project provides a comprehensive visual analysis of the stock performance of five major US banks over a five-year period. Using Python with pandas, matplotlib, and seaborn, the script fetches historical stock data from a CSV file, processes it, and generates a 2x2 dashboard of insightful visualizations.

![Financial Analysis Dashboard](bank_data_visualization.jpg)

The final output is a single PNG image that includes:

    Price Distribution: A boxplot showing the distribution, median, and outliers of stock prices for each bank.

    Price Performance: A line chart tracking the closing price of each stock over the five-year period.

    Daily Volatility: A line chart showing the daily percentage returns, illustrating the volatility of each stock.

    Correlation Matrix: A heatmap visualizing the correlation between the daily returns of the different bank stocks.

Final Output
Features

    Data Processing: Loads and cleans data efficiently using the pandas library.

    Comprehensive Analysis: Generates four distinct plots to analyze the stocks from different perspectives (price, performance, volatility, and correlation).

    High-Quality Visuals: Uses Matplotlib and Seaborn to create a clean, professional, and easy-to-read dashboard.

    Modular Code: The script is well-structured with functions for data loading and visualization, making it easy to read and maintain.

    Reproducible: Fully self-contained and easy to run with a standard Python environment.

How to Run This Project

To run this analysis on your own machine, follow these steps:

1. Clone the Repository (or download the files):

2. Download the Dataset:

    Make sure you have the all_stocks_5yr.csv file in the same directory as the Python script.

3. Create and Activate a Virtual Environment:
It is highly recommended to use a virtual environment to manage project dependencies.

# Create the environment
python3 -m venv venv

# Activate it (on Linux/macOS)
source venv/bin/activate

# On Windows
.\venv\Scripts\activate

4. Install Dependencies:
The required packages are listed in requirements.txt. You can install them all with one command.

pip install -r requirements.txt

(If you don't have a requirements.txt file, you can create one after installing the packages manually with pip freeze > requirements.txt)

5. Run the Script:
Execute the Python script to generate the visualization.

python generate_visualizations.py

The script will print Visualization saved successfully as 'bank_data_visualization.png' and the image file will appear in your project directory.
Dependencies

    pandas

    matplotlib

    seaborn

    scipy
