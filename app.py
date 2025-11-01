from flask import Flask, request, render_template_string
import yfinance as yf

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Stock Price Viewer</title>
    <style>
        body {
            margin: 0;
            font-family: "Inter", sans-serif;
            background: linear-gradient(135deg, #1e1e2f, #2e335a);
            color: #e6e6f0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }

        .container {
            background: rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(10px);
            padding: 40px 60px;
            border-radius: 20px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            text-align: center;
            width: 400px;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .container:hover {
            transform: translateY(-4px);
            box-shadow: 0 12px 40px rgba(0, 0, 0, 0.4);
        }

        h1 {
            color: #00d9ff;
            font-size: 28px;
            margin-bottom: 25px;
        }

        form input[type="text"] {
            padding: 12px;
            width: 80%;
            border: none;
            border-radius: 10px;
            outline: none;
            font-size: 16px;
            background: rgba(255, 255, 255, 0.15);
            color: #fff;
            margin-bottom: 20px;
        }

        form input::placeholder {
            color: #c2c2c2;
        }

        form button {
            background: linear-gradient(90deg, #00d9ff, #4f9cff);
            border: none;
            border-radius: 10px;
            color: #fff;
            padding: 12px 20px;
            font-size: 16px;
            cursor: pointer;
            transition: 0.3s ease;
        }
        form button:hover {
            background: linear-gradient(90deg, #4f9cff, #00d9ff);
            transform: scale(1.05);
        }

        .result-card {
            background: rgba(255, 255, 255, 0.1);
            padding: 25px;
            border-radius: 15px;
            margin-top: 20px;
            animation: fadeIn 0.5s ease-in-out;
        }
        .result-card h2 {
            color: #00d9ff;
            font-size: 22px;
            margin-bottom: 8px;
        }
        .result-card h3 {
            color: #4f9cff;
            font-size: 28px;
            margin: 0;
        }

        .error {
            color: #ff6b6b;
            margin-top: 15px;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 Stock Price Viewer</h1>

        <form method="post">
            <input type="text" name="ticker" placeholder="Enter stock symbol (e.g. TSLA, INFY)" required>
            <button type="submit">Get Price</button>
        </form>

        {% if error %}
            <p class="error">{{ error }}</p>
        {% elif price %}
            <div class="result-card">
                <h2>{{ ticker }}</h2>
                <p>Current Price:</p>
                <h3>₹{{ price }}</h3>
            </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    price = None
    ticker = None
    error = None

    if request.method == "POST":
        ticker = request.form["ticker"].upper()
        try:
            data = yf.Ticker(ticker)
            hist = data.history(period="1d")
            if hist.empty:
                error = "❌ Invalid stock symbol or no data available."
            else:
                price = round(hist["Close"][0], 2)
        except Exception:
            error = "⚠️ Error fetching data. Please try again."

    return render_template_string(HTML_PAGE, price=price, ticker=ticker, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
