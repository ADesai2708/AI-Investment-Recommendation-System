import streamlit as st
from advisor import get_recommendation
from market import get_market_trends
from database import save_user, get_users
from chatbot import get_chatbot_response
import pandas as pd

# ✅ ONLY ONCE
st.set_page_config(page_title="AI Investment Advisor", layout="wide")

# ---------------- SIDEBAR ---------------- #
st.sidebar.title("👤 User Profile")

age = st.sidebar.slider("Age", 18, 70, 25, key="age")
income = st.sidebar.number_input("Monthly Income (₹)", min_value=10000, key="income")
risk_appetite = st.sidebar.selectbox(
    "Risk Appetite", ["Low", "Medium", "High"], key="risk"
)

st.sidebar.markdown("---")

page = st.sidebar.radio("Navigate", ["Advisor", "History", "Chatbot"], key="page")

# ---------------- PAGE 1: ADVISOR ---------------- #
if page == "Advisor":

    st.title("💰 AI Investment Advisor")

    col1, col2 = st.columns([2, 1])

    if st.button("🚀 Get Recommendation", key="recommend_btn"):

        strategy = get_recommendation(age, income)

        # Save to DB
        save_user(age, income, risk_appetite, strategy)

        with col1:
            st.subheader("📊 Recommended Strategy")
            st.success(strategy)

            # Portfolio Allocation
            st.subheader("📌 Suggested Portfolio")

            if risk_appetite == "Low":
                allocation = {"Bonds": 50, "FD": 30, "Gold": 20}
            elif risk_appetite == "Medium":
                allocation = {"Mutual Funds": 40, "Stocks": 40, "Gold": 20}
            else:
                allocation = {"Stocks": 60, "Crypto": 20, "ETFs": 20}

            df = pd.DataFrame(list(allocation.items()), columns=["Asset", "Percentage"])
            st.bar_chart(df.set_index("Asset"))

        with col2:
            st.subheader("📈 Market Trends")
            trends = get_market_trends()

            for stock, prices in trends.items():
                st.write(f"**{stock}**")
                st.line_chart(prices)

        # AI Explanation
        st.subheader("🧠 Why this recommendation?")

        st.info(f"""
        Based on your age ({age}) and income (₹{income}),
        you fall under a {risk_appetite.lower()} risk profile.

        ✔ Younger → more risk capacity  
        ✔ Higher income → more investment potential  
        ✔ Strategy balances safety and growth  
        """)

# ---------------- PAGE 2: HISTORY ---------------- #
elif page == "History":

    st.title("📊 User History")

    users = get_users()

    df = pd.DataFrame(users, columns=["ID", "Age", "Income", "Risk", "Strategy"])
    st.dataframe(df)

# ---------------- PAGE 3: CHATBOT ---------------- #
elif page == "Chatbot":

    st.title("🤖 AI Financial Assistant")

    user_input = st.text_input("Ask about investments:", key="chat_input")

    if st.button("Ask", key="ask_btn"):
        response = get_chatbot_response(user_input)
        st.success(response)