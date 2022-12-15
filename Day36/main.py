

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

from datetime import datetime

today = datetime.now()
# print(today.strftime("%Y-%m-%d"))
yesterday = (int(today.strftime("%d")))- 1
yesterday_formatted = today.strftime(f"%Y-%m-{yesterday}")
# print(yesterday_formatted)

day_before_yesterday = (int(today.strftime("%d")))- 2
day_before_yesterday_formatted = today.strftime(f"%Y-%m-{day_before_yesterday}")
# print(day_before_yesterday_formatted)


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
print(data)

stock_yesterday = data[yesterday_formatted]["4. close"]
stock_day_before_yesterday = data[day_before_yesterday_formatted]["4. close"]
print(stock_yesterday)
print(stock_day_before_yesterday)

price_difference = float(stock_yesterday) - float(stock_day_before_yesterday)
print(f"Price difference: {price_difference}")