import requests
from datetime import datetime, timedelta
from flight_data import FlightData

TEQ_QUERY_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
TEQ_SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
TEQ_API_KEY = "**************************************"


class FlightSearch(FlightData):

    def __init__(self):
        self.today = datetime.now()
        self.tomorrow = self.today + timedelta(1)
        self.six_months = self.tomorrow + timedelta(days=180)
        self.tomorrow_formatted = self.get_flight_date_range()["tomorrow"]
        self.six_months_formatted = self.get_flight_date_range()["six_months"]

    def call_tequila(self, city):
        """This function makes a request to Kiwi Partners Tequila API to get the city iata code"""

        tequila_parameters = {"term": city}
        headers = {"apikey": TEQ_API_KEY}

        iata_codes = requests.get(TEQ_QUERY_ENDPOINT, params=tequila_parameters, headers=headers)
        iata_codes.raise_for_status()
        data = iata_codes.json()['locations'][0]['code']
        return data

    def search_iata_code(self, sheety):
        """
        This function checks the sheety data to see if a city has an iata code
        and updates it by calling Tequila and adding the iata to sheety.
        """
        for city_name in sheety:
            if city_name['iataCode'] == '':
                iata = self.call_tequila(city_name['city'])
                city_name['iataCode'] = iata
        return sheety


    def get_flight_date_range(self):
        """ This gets the date range for the tequila search parameters """

        tomorrow_formatted = self.tomorrow.strftime("%d/%m/%Y") 
        six_months_formatted = self.six_months.strftime("%d/%m/%Y")
        return {"tomorrow": tomorrow_formatted, "six_months": six_months_formatted}

# SEARCH FLIGHT PRICES

    def search_cheap_flights(self, depart_city, arrival_city):
        """
        This function checks Tequila API for flight prices of the cities in the sheety data
         and returns data from the cheapest flights.
        """
        tequila_new_params = {
            "fly_from": depart_city,
            "fly_to":  arrival_city,
            "date_from": self.get_flight_date_range()["tomorrow"],
            "date_to": self.get_flight_date_range()["six_months"],
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "curr": "GBP",
            "max_stopovers": 0,
        }

        headers = {
            "apikey": TEQ_API_KEY,
            "Content-Type": "application/json",
        }

        flight_check = requests.get(TEQ_SEARCH_ENDPOINT, params=tequila_new_params, headers=headers)
        flight_check.raise_for_status()

        try:
            available_flights = flight_check.json()['data'][0]
        
        except IndexError:
            print(f"Flight to {arrival_city} is not available.") 
        
        flight_information = FlightData(price=available_flights['price'], 
                                    departure_city_name=available_flights['cityFrom'],
                                    departure_airport_iata_code=available_flights['flyFrom'],
                                    arrival_city_name=available_flights['cityTo'],
                                    arrival_airport_iata_code=available_flights['flyTo'],
                                    outbound_date=available_flights['local_departure'].split('T')[0],
                                    inbound_date=available_flights['local_arrival'].split('T')[0])

        print(f"Flight to {arrival_city}: GBP {flight_information.price}")
        return flight_information