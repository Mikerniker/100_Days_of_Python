import requests
from datetime import datetime, timedelta

TEQ_QUERY_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
TEQ_SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
TEQ_API_KEY = "**************************************"



class FlightSearch:

    def __init__(self):
        self.today = datetime.now()
        self.tomorrow = self.today + timedelta(1)
        self.six_months = self.tomorrow + timedelta(days=180)
        self.get_flight_date_range()

#TESTING CODE:
    def call_tequila(self, city):
        """This function makes a request to Kiwi Partners Tequila API to get the city iata code"""

        tequila_parameters = {
            "term": city
            }

        headers = {
            "apikey": TEQ_API_KEY,
            }

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

#SEARCH PRICES

    def get_flight_date_range(self):
        """ This gets the date range for the tequila search parameters """
        self.tomorrow_formatted = self.tomorrow.strftime("%d/%m/%Y")

        self.six_months_formatted = self.six_months.strftime("%d/%m/%Y")
        return {"tomorrow": self.tomorrow_formatted, "six_months": self.six_months_formatted}


