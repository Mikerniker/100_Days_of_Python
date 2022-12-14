

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

from datetime import datetime

today = datetime.now()
print(today.strftime("%Y-%m-%d"))
yesterday = (int(today.strftime("%d")))- 1
print(yesterday)
print(today.strftime(f"%Y-%m-{yesterday}"))



import requests

API = ""

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": API
}

url = 'https://www.alphavantage.co/query'

stock_data = requests.get(url, params=stock_params)
stock_data.raise_for_status()
data = stock_data.json()['Time Series (Daily)']
# print(data)
