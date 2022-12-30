import requests
from pprint import pprint
from flight_search import FlightSearch
from data_manager import DataManager

#Get sheety data

SHEETY_URL = 'https://api.sheety.co/#insertsheetyurl'

sheety_table = requests.get(SHEETY_URL)

sheety_table.raise_for_status()
sheet_data = sheety_table.json()['sheet1']
pprint(sheet_data)

all_prices = [item['lowestPrice'] for item in sheet_data]
print(all_prices)

#Search for flights
# flights = FlightSearch()
# pprint(flights.add_iata_code(sheet_data))


#Add to sheety spreadsheet
# managed_data = DataManager()
# print(managed_data.add_iatacode_to_sheet(SHEETY_URL, sheet_data).text)

#Update iata codes in sheet data
flights = FlightSearch()
sheet_data = flights.search_iata_code(sheet_data)
pprint(sheet_data)

#Add changes to Sheety
managed_data = DataManager()
managed_data.add_iatacode_to_sheet(SHEETY_URL, sheet_data)


#TESTING STEP 4:

from datetime import datetime, timedelta

today = datetime.now()

print(today.strftime("%d/%m/%Y"))

tomorrow = today + timedelta(1)
print(tomorrow.strftime("%d/%m/%Y"))

six_months = tomorrow + timedelta(days=180)
print(six_months.strftime("%d/%m/%Y"))

tequila_newparameters = {
    "fly_from": "LON",
    "fly_to":  city,
    "date_from": tomorrow,
    "date_to": six_months,
    "nights_in_dst_from": 7,
    "nights_in_dst_to": 28,
    "flight_type": round,
    "one_for_city": 1,
    "curr": "GBP",
    "max_stopovers": 0,
}
