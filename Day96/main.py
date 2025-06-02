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
        'Raw': (
            item['ConversionInfo']['RAW'][0]
            if 'RAW' in item['ConversionInfo'] else None
        ),

    }
    for item in all_data
])

st.markdown("## TEST TABLE Top Gainers")

for _, row in df.iterrows():
    col1, col2, col3, col4, col5, col6 = st.columns([1, 2, 3, 2, 2, 3])

    with col1:
        st.image(row['Image URL'], width=40)
    with col2:
        st.write(row['Symbol'])
    with col3:
        st.write(row['Full Name'])
