import requests
from pprint import pprint
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

flights = FlightSearch()
managed_data = DataManager()
notify = NotificationManager()

#Get sheety data

SHEETY_URL = 'https://api.sheety.co/#insertsheetyurl'

sheety_table = requests.get(SHEETY_URL)

sheety_table.raise_for_status()
sheet_data = sheety_table.json()['sheet1']
pprint(sheet_data)

# Look for IATA Codes
sheet_data = flights.search_iata_code(sheet_data)
# pprint(sheet_data)

# Put IATA Codes in Sheety
managed_data.add_iatacode_to_sheet(SHEETY_URL, sheet_data)

# Search for Cheap Flights and send notification

DEPART_FROM = "LON"

for item in sheet_data:
    available_flights = flights.search_cheap_flights(DEPART_FROM, item['iataCode'])
    if item['lowestPrice'] > available_flights.price:
        alert = f"Low price alert! Only Gbp {available_flights.price} to fly from " \
                f"{available_flights.departure_city_name}-" \
                f"{available_flights.arrival_city_name} " \
                f"to {available_flights.departure_airport_iata_code}-" \
                f"{available_flights.arrival_airport_iata_code}, " \
                f"from {available_flights.outbound_date} to " \
                f"{available_flights.inbound_date}"
        notify.send_telegram_message(alert)
        print(alert)
    else:
        print(f"A flight to {available_flights.arrival_city_name} is {available_flights.price}. That's too expensive")



