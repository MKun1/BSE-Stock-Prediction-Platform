# BSE-Stock-Prediction-Platform

**📈 BSE Stock Price Prediction Platform
A machine learning-powered web application for predicting Bombay Stock Exchange (BSE) stock prices**

**✨ Features**
**Core Functionalities**


📊 Stock Prediction API

Predict prices for 1 day, 1 week, or 1 month horizons

Visualize historical trends and future forecasts

Percentage change calculations for quick insights

📋 Supported Stocks

Pre-configured for 100+ major BSE stocks (RELIANCE, TCS, HDFCBANK, etc.)

Easy-to-use stock code lookup

📩 Contact Management

Secure form submissions stored in SQLite

Admin interface for message tracking

**🛠 Technologies Used**
Category	Technologies
Frontend	HTML5, CSS3, JavaScript (Bootstrap 5)
Backend	Python (Flask), Flask-CORS
Database	SQLite
ML Engine	TensorFlow/Keras, Scikit-learn
Deployment	Render (or Vercel/Heroku)


**🚀 Quick Start**
1. Clone the Repository
bash
git clone https://github.com/your-username/BSE-Stock-Price-Prediction.git
cd BSE-Stock-Price-Prediction
2. Set Up Environment
bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
3. Run the Application
bash
python app.py
Access at: http://127.0.0.1:5000

**🔌 API Documentation**
GET /getStockCodes
Response:

json
{
  "codes": ["RELIANCE", "TCS", "HDFCBANK", ...]
}
POST /predict
Request:

json
{
  "stock": "RELIANCE",
  "timeframe": "1week"
}
Response:

json
{
  "predicted_price": 2870.45,
  "percentage_change": 2.45,
  "historical_data": [...],
  "forecast_dates": [...]
}
POST /contact
Request:

json
{
  "name": "John Doe",
  "email": "john@example.com",
  "message": "Feedback text"
}
🗃 Database Schema
sql
CREATE TABLE messages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    subject TEXT NOT NULL,
    message TEXT NOT NULL,
    submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


**☁ Deployment (Render)**
Push to GitHub

Create new Web Service on Render

Configure:

Build Command: pip install -r requirements.txt

Start Command: gunicorn app:app

**🤝 Contributing**
Fork the repository

Create a feature branch:

bash
git checkout -b feature/awesome-feature
Submit a PR with clear descriptions

**📜 License**
MIT License - See LICENSE

📬 Contact
Email: kundaimduduzi2@gmail.com
Issues: GitHub Issues

