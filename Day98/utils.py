import requests
import requests


def get_btc_info():
    url = "https://api.coingecko.com/api/v3/coins/bitcoin"
    response = requests.get(url)
    data = response.json()



# def check_price(change, symbol): 
#     threshold = 5  # percent
#     if change is None:
#         return
    
#     if change <= -threshold:
#         st.warning(f"🔻 {symbol} dropped more than {threshold}% in the last 24 hours")
#     elif change >= threshold:
#         st.success(f"🔺 {symbol} rose more than {threshold}% in the last 24 hours")

