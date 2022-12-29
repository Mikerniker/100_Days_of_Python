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