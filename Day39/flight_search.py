class FlightSearch:

    def add_iata_code(self, data):
        for item in data:
            if item['iataCode'] == '':
                item['iataCode'] = "TESTING"
        return data
