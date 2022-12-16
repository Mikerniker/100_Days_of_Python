import requests
from datetime import datetime


TELEGRAM_CHAT_ID = "insert id"
TELEGRAM_TOKEN = "add your token"
ALPHAVANTAGE_API = ""
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
NEWS_API = ""  #insert api
alphavantage_url = 'https://www.alphavantage.co/query'
news_url = 'https://newsapi.org/v2/everything'

def send_telegram_message(message):
    parameters = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
    }

    response = requests.post(url=f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage", params=parameters)
    response.raise_for_status()
    data = response.json()
    return data


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").


today = datetime.now()
# print(today.strftime("%Y-%m-%d"))
yesterday = (int(today.strftime("%d")))- 1
yesterday_formatted = today.strftime(f"%Y-%m-{yesterday}")
# print(yesterday_formatted)

day_before_yesterday = (int(today.strftime("%d")))- 2
day_before_yesterday_formatted = today.strftime(f"%Y-%m-{day_before_yesterday}")
# print(day_before_yesterday_formatted)



stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": ALPHAVANTAGE_API,
}


stock_data = requests.get(alphavantage_url, params=stock_params)
stock_data.raise_for_status()
data = stock_data.json()['Time Series (Daily)']
print(data)

stock_yesterday = data[yesterday_formatted]["4. close"]
stock_day_before_yesterday = data[day_before_yesterday_formatted]["4. close"]
print(stock_yesterday)
print(stock_day_before_yesterday)

price_difference = float(stock_yesterday) - float(stock_day_before_yesterday)
print(f"Price difference: {price_difference}")
percent_diff = abs(price_difference / float(stock_yesterday) * 100)
print("Percent:" + str(percent_diff))


# STEP 2 GET NEWS: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


# def get_news():
news_params = {
    "q": COMPANY_NAME,
    "from": yesterday_formatted,
    "to": day_before_yesterday_formatted,
    "language": "en",
    "sortBy": "relevancy",
    "pageSize": 3,
    "apiKey": NEWS_API,
}
request = requests.get(news_url, params=news_params)
request.raise_for_status()
news_data = request.json()['articles']


# def stock_changed():
if percent_diff == 5:
    for article in range(3):
        title = news_data[article]['title']
        brief = news_data[article]['description']
        message = f"{STOCK}: \n Headline: {title} \n Brief: {brief}"
        send_telegram_message(message)

else:
    send_telegram_message("No significant change")



