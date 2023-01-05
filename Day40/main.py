import requests
from pprint import pprint
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager


flights = FlightSearch()
managed_data = DataManager()
notify = NotificationManager()


SHEETY_URL = 'https://api.sheety.co/<addSHEETYURL>'

sheety_table = requests.get(SHEETY_URL)

sheety_table.raise_for_status()
sheet_data = sheety_table.json()['prices']
# pprint(sheet_data)

# Look for IATA Codes
# sheet_data = flights.search_iata_code(sheet_data)
# pprint(sheet_data)

# Put IATA Codes in Sheety
# managed_data.add_iatacode_to_sheet(SHEETY_URL, sheet_data)


# Search for Cheap Flights and send notification

DEPART_FROM = "LON"
stopovers = 0

for item in sheet_data:
    
    all_available_flights = flights.search_cheap_flights(DEPART_FROM, item['iataCode'], stopovers)

    if all_available_flights:
        if item['lowestPrice'] > all_available_flights.price:
            alert = f"Low price alert! Only Gbp {all_available_flights.price} to fly from " \
                    f"{all_available_flights.departure_city_name}-" \
                    f"{all_available_flights.arrival_city_name} " \
                    f"to {all_available_flights.departure_airport_iata_code}-" \
                    f"{all_available_flights.arrival_airport_iata_code}, " \
                    f"from {all_available_flights.outbound_date} to " \
                    f"{all_available_flights.inbound_date}"
            notify.send_telegram_message(alert)
            print(alert)
        else:
            print(f"A flight to {all_available_flights.arrival_city_name} is {all_available_flights.price}. That's too expensive")
    else:
        all_available_flights = flights.search_cheap_flights(DEPART_FROM, item['iataCode'], stopovers=2)
        print(f"Low price alert! Only Gbp £{all_available_flights.price} to fly from "
                f"{all_available_flights.departure_city_name}-{all_available_flights.arrival_city_name} "
                f"to {all_available_flights.departure_airport_iata_code}-"
                f"{all_available_flights.arrival_airport_iata_code},"
                f"from {all_available_flights.outbound_date} to {all_available_flights.inbound_date}. "
                f"This flight has {all_available_flights.stop_overs + 2} stop over/s, via "
                f"{all_available_flights.via_city}.")