import requests
from datetime import datetime
import os


APP_ID = os.environ["SHEETLY_APP_ID"]

API_KEY = os.environ["SHEETLY_API_KEY"]

URL = " https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_config = {
   "query": input("What exercises did you do?: "),
}


# With Authentication / Authorization
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Authorization": os.environ.get("SHEETLY_AUTH_TOKEN")
}

response = requests.post(url=URL, json=exercise_config, headers=headers)
print(response.text)
data = response.json()
# print(data["exercises"])

user_input = data["exercises"][0]["user_input"].title()
duration = data["exercises"][0]["duration_min"]
calories = data["exercises"][0]["nf_calories"]
# print(f"Exercise: {user_input}, Duration: {duration}, Calories: {calories}")

date = datetime.now()
formatted_date = date.strftime("%d/%m/%Y")
time = date.strftime("%H:%M:%S")
# print(date)

row_sheet_api = os.environ.get("SHEETLY_ROW_SHEET_API")

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

new_response = requests.post(url=row_sheet_api, json=workout_data, headers=headers)
print(new_response.text)
