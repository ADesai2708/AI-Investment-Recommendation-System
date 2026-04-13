from pyswip import Prolog

prolog = Prolog()
prolog.consult("rules.pl")

def get_recommendation(age, income):
    query = f"recommend({age}, {income}, Strategy)"
    result = list(prolog.query(query))
    
    if result:
        return result[0]['Strategy']
    return "No recommendation found"

import yfinance as yf

def get_market_trends():
    stocks = ["AAPL", "TSLA", "^GSPC"]
    data = {}

    for stock in stocks:
        ticker = yf.Ticker(stock)
        hist = ticker.history(period="5d")
        data[stock] = hist["Close"].tolist()

    return data