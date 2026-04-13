def get_chatbot_response(user_input):
    user_input = user_input.lower()

    if "investment" in user_input:
        return "Diversification is key! Spread your investments across assets."

    elif "risk" in user_input:
        return "Higher risk can give higher returns, but also higher losses."

    elif "stocks" in user_input:
        return "Stocks are great for long-term growth but can be volatile."

    elif "safe" in user_input:
        return "Fixed deposits and bonds are safer investment options."

    else:
        return "I can help with investments, risk, stocks, and finance tips!"