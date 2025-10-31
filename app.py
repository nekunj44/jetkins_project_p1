from flask import Flask, render_template_string, request
import yfinance as yf

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Stock Price Viewer</title>
</head>
<body style="text-align:center; font-family:Arial;">
    <h1>📈 Stock Price Viewer</h1>
    <form method="post">
        <input type="text" name="ticker" placeholder="Enter stock symbol (e.g. TSLA, INFY)" required>
        <input type="submit" value="Get Price">
    </form>
    {% if price %}
        <h2>Current price of {{ ticker }}: ₹{{ price }}</h2>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    price = None
    ticker = None
    if request.method == "POST":
        ticker = request.form["ticker"].upper()
        try:
            data = yf.Ticker(ticker)
            price = round(data.history(period="1d")["Close"][0], 2)
        except Exception:
            price = "Error fetching data"
    return render_template_string(HTML_TEMPLATE, price=price, ticker=ticker)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
