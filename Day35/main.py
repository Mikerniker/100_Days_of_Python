import requests
import os


TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")


def send_telegram_message(message):
    parameters = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message,
    }

    response = requests.post(url=f"https://api.telegram.org/bot{TOKEN}/sendMessage", params=parameters)
    response.raise_for_status()
    data = response.json()
    return data

# Send a Telegram sticker (optional)
def send_telegram_sticker():
    new_parameters = {
        "chat_id": TELEGRAM_CHAT_ID,
        "sticker": "CAACAgIAAxkBAAMIY5eEkgzIWhbUHzVBwrEvoO1I4A4AAiYBAAKmREgLTZCtuf2gbdorBA",
    }

    response2 = requests.post(url=f"https://api.telegram.org/bot{TOKEN}/sendSticker", params=new_parameters)
    response2.raise_for_status()
    data2 = response2.json()
    return data2

# Open Weather Map API

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = os.environ.get("OWM_API_KEY")

weather_params = {
    "lat": 14.676041,
    "lon": 121.043701,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

list_of_twelve_hours = weather_data["hourly"][0:12]
will_rain = False
for hour in list_of_twelve_hours:
    condition_code = hour["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    message = "It's going to rain, don't forget to bring an umbrella!"
    send_telegram_message(message)
    send_telegram_sticker()
