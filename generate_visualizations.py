import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os # Import the 'os' module to handle file paths

def load_and_prepare_data(filepath, tickers):
    """
    Loads stock data from a CSV file, filters for specific tickers,
    and pivots the data into a clean, wide format.

    Args:
        filepath (str): The path to the CSV file.
        tickers (list): A list of stock ticker symbols to filter for.

    Returns:
        pandas.DataFrame: A cleaned DataFrame with dates as the index and
                          stock prices in columns for each ticker. Returns None
                          if the file is not found.
    """
    try:
        # Load the entire dataset from the CSV file
        all_data = pd.read_csv(filepath)
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.")
        # Exit the script if the data file is not available
        sys.exit(1)

    # Filter the DataFrame to include only the rows with the specified tickers
    bank_data_raw = all_data[all_data['Name'].isin(tickers)].copy()

    # Convert the 'date' column to datetime objects for proper time-series analysis
    bank_data_raw['date'] = pd.to_datetime(bank_data_raw['date'])

    # Pivot the table to create a "wide" format DataFrame.
    # This structure is ideal for plotting, with dates as the index
    # and a separate column for each ticker's closing price.
    bank_data_clean = bank_data_raw.pivot(index='date', columns='Name', values='close')

    return bank_data_clean

def create_visualizations(df, tickers, output_filename):
    """
    Generates and saves a 2x2 grid of plots (boxplot, line plot, daily returns, correlation heatmap).

    Args:
        df (pandas.DataFrame): The cleaned DataFrame containing stock data.
        tickers (list): A list of stock ticker symbols for labels.
        output_filename (str): The filename for the saved image.
    """
    # Use a professional plot style for better aesthetics
    plt.style.use('seaborn-v0_8-whitegrid')

    # Create a figure and a 2x2 grid of subplots using the object-oriented approach
    fig, ax = plt.subplots(2, 2, figsize=(20, 15))

    # --- Subplot 1: Boxplot (Top-Left) ---
    # Visualizes the distribution, median, and outliers for each stock.
    ax[0, 0].boxplot(df.dropna())
    ax[0, 0].set_title('Distribution of Bank Stock Prices (5-Year)', fontsize=16)
    ax[0, 0].set_ylabel('Stock Price (USD)', fontsize=12)
    ax[0, 0].set_xticklabels(tickers)

    # --- Subplot 2: Line Plot (Top-Right) ---
    # Shows the performance of each stock over time.
    ax[0, 1].plot(df)
    ax[0, 1].set_title('Bank Stock Price Performance (5-Year)', fontsize=16)
    ax[0, 1].set_xlabel('Date', fontsize=12)
    ax[0, 1].set_ylabel('Stock Price (USD)', fontsize=12)
    ax[0, 1].legend(tickers)

    # --- Subplot 3: Daily Returns (Bottom-Left) ---
    # Calculate and plot the daily percentage change to show volatility.
    daily_returns = df.pct_change()
    for ticker in tickers:
        ax[1, 0].plot(daily_returns[ticker], label=ticker, alpha=0.8)
    ax[1, 0].set_title('Daily Returns (Volatility)', fontsize=16)
    ax[1, 0].set_ylabel('Percentage Change', fontsize=12)
    ax[1, 0].set_xlabel('Date', fontsize=12)
    ax[1, 0].legend()

    # --- Subplot 4: Correlation Heatmap (Bottom-Right) ---
    # A heatmap provides a clear visual of how the stocks' daily returns correlate.
    corr = daily_returns.corr()
    sns.heatmap(corr, ax=ax[1, 1], annot=True, cmap='coolwarm', fmt=".2f")
    ax[1, 1].set_title('Correlation Matrix of Daily Returns', fontsize=16)
    
    # Add a main title to the entire figure
    fig.suptitle('Financial Analysis of Major US Banks', fontsize=24, fontweight='bold')

    # Adjust layout to prevent titles and labels from overlapping
    fig.tight_layout(rect=[0, 0.03, 1, 0.96]) # Adjust rect to make space for suptitle

    # Save the generated figure to a file
    try:
        plt.savefig(output_filename, dpi=300) # Use higher DPI for better quality
        print(f"Visualization saved successfully as '{output_filename}'")
    except Exception as e:
        print(f"Error saving the file: {e}")


def main():
    """
    Main function to execute the data loading and visualization script.
    """
    # --- Configuration ---
    # Get the absolute path of the directory where the script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Join the script directory path with the CSV file name
    FILEPATH = os.path.join(script_dir, 'all_stocks_5yr.csv')
    
    TICKERS = ['JPM', 'BAC', 'C', 'WFC', 'GS']
    OUTPUT_FILENAME = os.path.join(script_dir, 'bank_data_visualization.png')

    # --- Execution ---
    # Step 1: Load and process the data
    bank_data = load_and_prepare_data(FILEPATH, TICKERS)

    # Step 2: Create and save the visualizations
    if bank_data is not None:
        create_visualizations(bank_data, TICKERS, OUTPUT_FILENAME)

# This standard Python construct ensures that the main() function is called
# only when the script is executed directly (not when imported as a module).
if __name__ == "__main__":
    main()
