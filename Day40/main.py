import requests
from customers import get_customer_email
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

def alert_customer(price, departure_city, arrival_city, depart_iata, arrive_iata, outbound, inbound):
    alert = f"Low price alert! Only Gbp £{price} to fly from " \
            f"{departure_city}-{arrival_city} to {depart_iata}-{arrive_iata}, from {outbound} to " \
            f"{inbound} Link: https://www.google.co.uk/flights?hl=en#flt=" \
            f"{depart_iata}.{arrive_iata}.{outbound}*{arrive_iata}.{depart_iata}.{inbound}"
    return alert


for item in sheet_data:
    
    all_available_flights = flights.search_cheap_flights(DEPART_FROM, item['iataCode'], stopovers)

    if all_available_flights:
        if item['lowestPrice'] > all_available_flights.price:
            message = alert_customer(all_available_flights.price, 
                            all_available_flights.departure_city_name,
                            all_available_flights.arrival_city_name,
                            all_available_flights.departure_airport_iata_code,
                            all_available_flights.arrival_airport_iata_code,
                            all_available_flights.outbound_date, all_available_flights.inbound_date)

            # notify.send_telegram_message(message)
            for i in get_customer_email():
                email = i['email']
                notify.send_emails(message, email)
        else:
            print(f"A flight to {all_available_flights.arrival_city_name} is {all_available_flights.price}. That's too expensive")
    else:
        all_available_flights = flights.search_cheap_flights(DEPART_FROM, item['iataCode'], stopovers=2)
        message = alert_customer(all_available_flights.price, all_available_flights.departure_city_name,
                            all_available_flights.arrival_city_name,
                            all_available_flights.departure_airport_iata_code,
                            all_available_flights.arrival_airport_iata_code,
                            all_available_flights.outbound_date, all_available_flights.inbound_date)
        for i in get_customer_email():
            email = i['email']
            notify.send_emails(message, email)
        notify.send_telegram_message(message)