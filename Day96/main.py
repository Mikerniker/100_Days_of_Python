import streamlit as st
import pandas as pd
import requests

URL = "https://min-api.cryptocompare.com/data/top/percent?limit=10&tsym=USD"

response = requests.get(url=URL)
response.raise_for_status()
data = response.json()
print(data["Data"])
all_data = data["Data"]


st.title("Top Crypto Gainers & Losers (24h)")

df = pd.DataFrame([
    {
        'Symbol': item['CoinInfo'].get('Name'),
        'Full Name': item['CoinInfo'].get('FullName'),
        'Image URL': "https://www.cryptocompare.com" + item['CoinInfo'].get('ImageUrl', ''),
        'Supply': item['ConversionInfo'].get('Supply'),
        'Total Volume 24H': item['ConversionInfo'].get('TotalVolume24H'),
    }
    for item in all_data
])


