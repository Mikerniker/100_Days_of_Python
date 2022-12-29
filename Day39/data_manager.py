import requests

class DataManager:

    def add_iatacode_to_sheet(self, url, sheety):
        """This function adds the iataCode to the Google sheet."""
        for city in sheety:
            new_url = f"{url}/{city['id']}"
            flight_codes = {
                "sheet1": {
                    "iataCode": city['iataCode'],
                }
            }
            edit_sheety_row = requests.put(url=new_url, json=flight_codes)
        return edit_sheety_row

