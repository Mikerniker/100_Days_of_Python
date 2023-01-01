class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self, price, departure_city_name, departure_airport_iata_code,
                 arrival_city_name, arrival_airport_iata_code, outbound_date, inbound_date):
        self.price = price
        self.departure_city_name = departure_city_name
        self.departure_airport_iata_code = departure_airport_iata_code
        self.arrival_city_name = arrival_city_name
        self.arrival_airport_iata_code = arrival_airport_iata_code
        self.outbound_date = outbound_date
        self.inbound_date = inbound_date

