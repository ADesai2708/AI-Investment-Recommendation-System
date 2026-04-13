import yfinance as yf

def get_market_trends():
    stocks = ["AAPL", "TSLA", "^GSPC"]
    data = {}

    for stock in stocks:
        ticker = yf.Ticker(stock)
        hist = ticker.history(period="5d")
        data[stock] = hist["Close"].tolist()

    return data