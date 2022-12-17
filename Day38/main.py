import requests
from datetime import datetime
import os


APP_ID = os.environ["SHEETLY_APP_ID"]
API_KEY = os.environ["SHEETLY_API_KEY"]
NUTRITIONIX_URL_ENDPOINT = " https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT_API = os.environ.get("SHEETLY_ROW_SHEET_API")

exercise_config = {
   "query": input("What exercises did you do (you can include duration and/or distance)?: "),
}

# With Authentication / Authorization
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Authorization": os.environ.get("SHEETLY_AUTH_TOKEN")
}

response = requests.post(url=NUTRITIONIX_URL_ENDPOINT, json=exercise_config, headers=headers)
#print(response.text)
data = response.json()
# print(data["exercises"])

user_input = data["exercises"][0]["user_input"].title()
duration = data["exercises"][0]["duration_min"]
calories = data["exercises"][0]["nf_calories"]
# print(f"Exercise: {user_input}, Duration: {duration}, Calories: {calories}")

#Record current date and time
date = datetime.now()
formatted_date = date.strftime("%d/%m/%Y")
time = date.strftime("%H:%M:%S")
# print(date)

workout_data = {
    "workout": {
      "date": formatted_date,
      "time": time,
      "exercise": user_input,
      "duration": duration,
      "calories": calories,
    }
  }

# Add new row to the spreadsheet with inputted data
new_response = requests.post(url=SHEETY_ENDPOINT_API, json=workout_data, headers=headers)
print(new_response.text)
