import requests

def get_btc_info():
    url = "https://api.coingecko.com/api/v3/coins/bitcoin"
    response = requests.get(url)
    data = response.json()

    info = {
        "name": data["name"],
        "symbol": data["symbol"],
        "logo": data["image"]["large"],
        "current_price": data["market_data"]["current_price"]["usd"],
        "price_change_24h": data["market_data"]["price_change_percentage_24h"],
        # "market_cap": data["market_data"]["market_cap"]["usd"],
    }

    return info


# def check_price(change, symbol): 
#     threshold = 5  # percent
#     if change is None:
#         return
    
#     if change <= -threshold:
#         st.warning(f"🔻 {symbol} dropped more than {threshold}% in the last 24 hours")
#     elif change >= threshold:
#         st.success(f"🔺 {symbol} rose more than {threshold}% in the last 24 hours")

