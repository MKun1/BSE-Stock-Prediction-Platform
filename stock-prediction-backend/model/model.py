from tensorflow.keras.models import load_model
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import requests
import pandas as pd
import os

# Load the pre-trained LSTM model

from tensorflow.keras.saving import load_model
trained_model = load_model('model/lstm_model_v3.keras')  # New path




# Initialize the scaler (same configuration used during model training)
scaler = MinMaxScaler(feature_range=(0, 1))

def preprocess_data(stock, timeframe, time_step):
    # Fetch historical prices and dates
    dates, historical_prices = get_historical_prices(stock, timeframe)

    # Check if we have enough data for the given time_step
    if len(historical_prices) < time_step:
        raise ValueError(
            f"Not enough historical data to create input sequence from Preprocess. "
            f"Available data points: {len(historical_prices)}, Required: {time_step}"
        )

    # Scale historical prices
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_prices = scaler.fit_transform(np.array(historical_prices).reshape(-1, 1))
    
    # Prepare the input sequence for prediction
    input_sequence = scaled_prices[-time_step:]  # Extract the required time_step window
    
    return input_sequence.reshape(1, time_step, 1), scaler






def calculate_percentage_change(predicted_price, historical_price):
    return ((predicted_price - historical_price) / historical_price) * 100


import yfinance as yf

def get_historical_prices(stock_symbol, timeframe):
    """
    Fetch historical stock prices dynamically based on the timeframe.
    Args:
        stock_symbol (str): Stock symbol (e.g., 'MARUTI.NS').
        timeframe (str): Time range for data (e.g., '1day', '1week', '1month').
    Returns:
        tuple: List of dates and closing prices for the requested timeframe.
    """
    print(f"Fetching data for stock: {stock_symbol}, timeframe: {timeframe}")
    stock_data = yf.Ticker(stock_symbol)
    
    if timeframe == "1day":
        historical_data = stock_data.history(period="30d")
    elif timeframe == "1week":
        historical_data = stock_data.history(period="100d")
    elif timeframe == "1month":
        historical_data = stock_data.history(period="200d")
    else:
        raise ValueError(f"Invalid timeframe specified: {timeframe}")
    
    dates = historical_data.index.tolist()  # Extract dates
    closing_prices = historical_data['Close'].tolist()  # Extract closing prices
    print(f"Fetched dates: {dates}")
    print(f"Fetched prices: {closing_prices}")
    return dates, closing_prices





import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt

import os

def plot_time_series_comparison(dates, historical_prices, predicted_prices, stock, window_size=7):
    """
    Plot smoothed actual vs. dynamically predicted stock prices and save the plot as an image.
    Args:
        dates (list): List of dates corresponding to historical prices.
        historical_prices (list): Actual closing prices.
        predicted_prices (list): Dynamically predicted prices.
        stock (str): Stock symbol for the title.
        window_size (int): Size of the moving average window for smoothing actual prices.
    Returns:
        str: URL to the saved plot image.
    """
    # Smooth the historical prices using a moving average
    smoothed_prices = pd.Series(historical_prices).ewm(span=window_size, adjust=False).mean().tolist()


    # Replace None values in predicted_prices with NaN (to avoid plotting errors)
    predicted_prices = [np.nan if price is None else price for price in predicted_prices]

    # Create the plot
    plt.figure(figsize=(14, 7))
    plt.plot(dates, smoothed_prices, label='Smoothed Actual Prices', color='blue', alpha=0.7)
    plt.plot(dates[-len(predicted_prices):], predicted_prices, label='Predicted Prices', color='red', linestyle='--', alpha=0.7)

    # Add plot details
    plt.title(f'{stock} Stock Price: Smoothed Actual vs. Predicted')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.tight_layout()

    # Save the plot to an image file
    image_path = f"static/plots/{stock}_comparison_plot.png"
    os.makedirs(os.path.dirname(image_path), exist_ok=True)
    plt.savefig(image_path)
    plt.close()

    # Correctly format the full URL for frontend use
    base_url = "http://127.0.0.1:5000"
    image_url = f"{base_url}/{image_path.lstrip('/')}"  # Ensure no double '//'
    return image_url





#Alternative way to generate predicitons function not in use
def generate_dynamic_predictions(historical_prices, trained_model, scaler, time_step):
    """
    Generate dynamic predictions for each time step based on historical data.
    Args:
        historical_prices (list): List of historical closing prices.
        trained_model (keras.Model): Pretrained LSTM model.
        scaler (MinMaxScaler): Scaler used for normalization and inverse transformation.
        time_step (int): Number of steps in the input sequence.
    Returns:
        list: List of predicted prices.
    """
    predictions = []
    scaled_prices = scaler.fit_transform(np.array(historical_prices).reshape(-1, 1))
    
    for i in range(time_step, len(historical_prices)):
        # Prepare input sequence for prediction
        input_sequence = scaled_prices[i-time_step:i].reshape(1, time_step, 1)
        
        # Predict the next price
        predicted_scaled = trained_model.predict(input_sequence)[0][0]
        predicted_price = scaler.inverse_transform([[predicted_scaled]])[0][0]
        predictions.append(predicted_price)

    # Pad initial steps with None to align with historical data
    return [None] * time_step + predictions

import numpy as np

def generate_full_predictions(historical_prices, trained_model, scaler, time_step):
    """
    Generate predictions that cover the entire time period using a rolling window.
    Args:
        historical_prices (list): List of historical closing prices.
        trained_model: Pretrained LSTM model.
        scaler (MinMaxScaler): Scaler for normalization and inverse transformation.
        time_step (int): Number of steps in the input sequence.
    Returns:
        list: Full list of predicted prices for the entire time period.
    """
    predictions = []
    scaled_prices = scaler.fit_transform(np.array(historical_prices).reshape(-1, 1))
    
    for i in range(time_step, len(historical_prices)):
        # Prepare input sequence for prediction
        input_sequence = scaled_prices[i-time_step:i].reshape(1, time_step, 1)
        
        # Predict the next price
        predicted_scaled = trained_model.predict(input_sequence)[0][0]
        predicted_price = scaler.inverse_transform([[predicted_scaled]])[0][0]
        predictions.append(predicted_price)

    # Pad initial steps with the first predicted value (or NaN if necessary)
    first_predicted_price = predictions[0] if predictions else np.nan
    return [first_predicted_price] * time_step + predictions

