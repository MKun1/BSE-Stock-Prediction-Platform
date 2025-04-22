from flask import Flask, jsonify, request
from tensorflow.keras.models import load_model
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from model.model import trained_model, preprocess_data, calculate_percentage_change, get_historical_prices, plot_time_series_comparison, generate_dynamic_predictions, generate_full_predictions

from flask_cors import CORS

app = Flask(__name__, static_url_path='/static')

CORS(app)




# Stock Codes Endpoint
@app.route('/getStockCodes', methods=['GET'])
def get_stock_codes():
    stock_codes = [
  "RELIANCE",
  "TCS",
  "HDFCBANK",
  "ICICIBANK",
  "INFY",
  "HINDUNILVR",
  "ITC",
  "BHARTIARTL",
  "SBIN",
  "LT",
  "KOTAKBANK",
  "AXISBANK",
  "BAJFINANCE",
  "ASIANPAINT",
  "M&M",
  "SUNPHARMA",
  "MARUTI",
  "TATAMOTORS",
  "NESTLEIND",
  "BAJAJFINSV",
  "POWERGRID",
  "NTPC",
  "ULTRACEMCO",
  "TITAN",
  "ADANIENT",
  "ADANIPORTS",
  "WIPRO",
  "HCLTECH",
  "TECHM",
  "INDUSINDBK",
  "GRASIM",
  "JSWSTEEL",
  "TATASTEEL",
  "BAJAJ-AUTO",
  "BRITANNIA",
  "CIPLA",
  "DRREDDY",
  "EICHERMOT",
  "HEROMOTOCO",
  "HINDALCO",
  "ONGC",
  "COALINDIA",
  "BPCL",
  "IOC",
  "GAIL",
  "DIVISLAB",
  "SBILIFE",
  "HDFCLIFE",
  "ICICIPRULI",
  "TATACONSUM",
  "VEDL",
  "UPL",
  "SHREECEM",
  "DABUR",
  "GODREJCP",
  "ZEEL",
  "AMBUJACEM",
  "ACC",
  "DLF",
  "TATAPOWER",
  "SIEMENS",
  "BOSCHLTD",
  "INFRATEL",
  "LUPIN",
  "AUROPHARMA",
  "ZYDUSLIFE",
  "BIOCON",
  "GLENMARK",
  "PIDILITIND",
  "COLPAL",
  "BERGEPAINT",
  "HAVELLS",
  "MOTHERSUMI",
  "ASHOKLEY",
  "BHARATFORG",
  "TATACHEM",
  "INDHOTEL",
  "PETRONET",
  "MUTHOOTFIN",
  "PAGEIND",
  "JUBLFOOD",
  "NAUKRI",
  "BANDHANBNK",
  "FEDERALBNK",
  "IDFCFIRSTB",
  "YESBANK",
  "PNB",
  "BANKBARODA",
  "CANBK",
  "UNIONBANK",
  "LICHSGFIN",
  "CHOLAFIN",
  "SRTRANSFIN",
  "ADANIGREEN",
  "ADANITRANS",
  "TATACOMM",
  "IDEA",
  "BHEL",
  "NMDC",
  "SAIL"
] # Expand this as needed
    return jsonify({"codes": stock_codes})




@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    stock = data.get('stock')
    timeframe = data.get('timeframe')

    if stock and timeframe:
        try:
            # Fetch historical data
            dates, historical_prices = get_historical_prices(stock, timeframe)

            # Set time_step
            time_step = {"1day": 5, "1week": 30, "1month": 60}.get(timeframe, None)
            if not time_step:
                return jsonify({"error": "Invalid timeframe specified. Please select 1day, 1week, or 1month."}), 400

            # Validate data length
            if len(historical_prices) < time_step:
                return jsonify({"error": f"Not enough historical data. Data points: {len(historical_prices)}, Required: {time_step}"}), 400

            # Preprocess data and generate predictions
            input_sequence, scaler = preprocess_data(stock, timeframe, time_step)
            predicted_prices = generate_full_predictions(historical_prices, trained_model, scaler, time_step)

            # Calculate percentage change
            predicted_price = predicted_prices[-1]
            historical_price = historical_prices[-1]
            percentage_change = calculate_percentage_change(predicted_price, historical_price)

            # Return raw data for frontend charting
            return jsonify({
                "stock": stock,
                "timeframe": timeframe,
                "predicted_price": round(predicted_price, 2),
                "percentage_change": round(percentage_change, 2),
                "dates": dates,
                "historical_prices": historical_prices,
                "predicted_prices": predicted_prices
            })

        except Exception as e:
            return jsonify({"error": f"An error occurred: {str(e)}"}), 500
    else:
        return jsonify({"error": "Invalid input. Stock and timeframe are required."}), 400


from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText


@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    subject = data.get('subject')
    message = data.get('message')

    if not name or not email or not subject or not message:
        return jsonify({"error": "All fields are required"}), 400

    # (Optional) Store to database here
    save_to_database(name, email, subject, message)

    return jsonify({"success": "Message received! We will get back to you shortly."}), 200





# saving the inputs to a database

import sqlite3

def save_to_database(name, email, subject, message):
    """
    Save the Contact Us form submission to the SQLite database.
    Args:
        name (str): User's name.
        email (str): User's email.
        subject (str): Subject of the message.
        message (str): User's message.
    """
    conn = sqlite3.connect('contact_us.db')
    cursor = conn.cursor()

    # Create the messages table if it doesn't already exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            subject TEXT NOT NULL,
            message TEXT NOT NULL,
            submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    # Insert the form data into the table
    cursor.execute('''
        INSERT INTO messages (name, email, subject, message) 
        VALUES (?, ?, ?, ?)
    ''', (name, email, subject, message))

    conn.commit()
    conn.close()


import os
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
