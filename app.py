from flask import Flask, render_template, request
import yfinance as yf

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route("/", methods=["GET", "POST"])
def home():
    price = None
    ticker = None
    error = None
    if request.method == "POST":
        ticker = request.form["ticker"].upper()
        try:
            data = yf.Ticker(ticker)
            price = round(data.history(period="1d")["Close"][0], 2)
        except Exception:
            error = "⚠️ Could not fetch data. Please check the stock symbol."
    return render_template("index.html", price=price, ticker=ticker, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
