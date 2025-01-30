import yfinance as yf
import streamlit as st

st.write("""
# Stock Price App

Shown are the stock ***closing price*** and ***volume***!

""")


options = [
"MSFT",
"TSLA",
"IBM",
"AAL",
"NOW",
"EVO.ST",
"XFOR",
"ATHE",
"NOK",
"WM",
"DGNX",
"UBER",
"NOKIA.HE",
"DJTWW",
"GOOG",
"CRGX",
"GOOGL"]

selected_option = st.selectbox("Select an option:", options)


tickerSymbol = selected_option
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)
