import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "my_api_key"

weather_params = {
    "lat": 14.676041,
    "lon": 121.043701,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

list_of_twelve = weather_data["hourly"][0:12]
will_rain = False
for i in list_of_twelve:
    condition_code = i["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")