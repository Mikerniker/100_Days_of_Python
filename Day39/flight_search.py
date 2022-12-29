import requests

TEQ_QUERY_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
TEQ_API_KEY = "**************************************"



class FlightSearch:

    # def add_iata_code(self, data):
    #     for item in data:
    #         if item['iataCode'] == '':
    #             item['iataCode'] = "TESTING"
    #     return data

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