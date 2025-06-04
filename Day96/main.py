import streamlit as st
import pandas as pd
import requests


URL = "https://min-api.cryptocompare.com/data/top/totalvolfull?limit=100&tsym=USD"

response = requests.get(url=URL)
response.raise_for_status()
data = response.json()
print(data["Data"])
all_data = data["Data"]

def format_money(value):
    if value is None:
        return "N/A"
    elif value >= 1_000_000_000:
        return f"${value / 1_000_000_000:.2f}B"
    elif value >= 1_000_000:
        return f"${value / 1_000_000:.2f}M"
    elif value >= 1_000:
        return f"${value / 1_000:.2f}K"
    else:
        return f"${value:.2f}"
    

cleaned_data = []

for item in all_data:
    coin = item.get('CoinInfo', {})
    conv = item.get('ConversionInfo', {})
    raw = conv.get('RAW', [])

    price = open_24h = change_24h = percent_change_24h = market_cap = None  # Initialize all

    if raw and isinstance(raw, list):
        try:
            parts = raw[0].split('~')
            price = float(parts[5])
            open_24h = float(parts[17])
            change_24h = price - open_24h
            percent_change_24h = (change_24h / open_24h * 100) if open_24h != 0 else 0
        except (IndexError, ValueError):
            pass

    supply = conv.get('Supply')
    if supply is not None and price is not None:
        try:
            market_cap = price * float(supply)
        except ValueError:
            market_cap = None

    cleaned_data.append({
        "Symbol": coin.get('Name'),
        "Full Name": coin.get('FullName'),
        "Image URL": "https://www.cryptocompare.com" + coin.get('ImageUrl', ''),
        "Supply": supply,
        "Total Vol 24H": conv.get('TotalVolume24H'),
        "Price": price,
        "Open 24h": open_24h,
        "Change 24h": change_24h,
        "Percent Change 24h": percent_change_24h,
        "Market Cap": market_cap
    })

df = pd.DataFrame(cleaned_data)
# print(df.to_string())

# Split Gainers & Losers
df = df.dropna(subset=["Percent Change 24h"])
top_gainers = df.sort_values(by="Percent Change 24h", ascending=False).head(10)
top_losers = df.sort_values(by="Percent Change 24h", ascending=True).head(10)


st.title("Top Crypto Gainers & Losers (24h)")


st.markdown("## TEST TABLE Top Gainers")

header_cols = st.columns([1, 2, 3, 2, 2, 3])
with header_cols[0]:
    st.markdown("**Logo**")
with header_cols[1]:
    st.markdown("**Symbol**")
with header_cols[2]:
    st.markdown("**Full Name**")
with header_cols[3]:
    st.markdown("**Price**")
with header_cols[4]:
    st.markdown("**24h % Change**")
with header_cols[5]:
    st.markdown("**Market Cap**")


for _, row in top_gainers.iterrows():
    col1, col2, col3, col4, col5, col6 = st.columns([1, 2, 3, 2, 2, 3])

    with col1:
        st.image(row['Image URL'], width=40)
    with col2:
        st.write(row['Symbol'])
    with col3:
        st.write(row['Full Name'])
    with col4:
        st.write(format_money(row['Price']))
    with col5:
        st.write(f"{row['Percent Change 24h']:.2f}%" if row['Percent Change 24h'] is not None else "N/A")
    with col6:
        st.write(format_money(row['Market Cap']))


# for _, row in df.iterrows():
#     col1, col2, col3, col4, col5, col6 = st.columns([1, 2, 3, 2, 2, 3])

#     with col1:
#         st.image(row['Image URL'], width=40)
#     with col2:
#         st.write(row['Symbol'])
#     with col3:
#         st.write(row['Full Name'])
