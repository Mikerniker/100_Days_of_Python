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
    def add_iata_code(self, data):
        cities = ["Paris", "Berlin", "Tokyo", "Sydney", "Istanbul", "Kuala Lumpur", "New York",
                  "San Francisco", "Cape Town"]
        for city in cities:
            tequila_parameters = {
                "term": city,
            }

            headers = {
                "apikey": TEQ_API_KEY,
            }

            iata_codes = requests.get(TEQ_QUERY_ENDPOINT, params=tequila_parameters, headers=headers)
            iata_codes.raise_for_status()
        data = iata_codes.json()
        return data
