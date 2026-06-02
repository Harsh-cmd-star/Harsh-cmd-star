import streamlit as st

st.set_page_config(
    page_title="AI Stock Research Assistant",
    page_icon="📈"
)

st.title("📈 AI Stock Research Assistant")

ticker = st.text_input(
    "Enter Stock Ticker",
    placeholder="AAPL"
)

if st.button("Analyze"):
    st.success(f"Analyzing {ticker}")
