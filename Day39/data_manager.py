import requests

class DataManager:

    def add_iatacode_to_sheet(self, url, data):
        for item in data:
            new_url = f"{url}/{item['id']}"
            flight_codes = {
                "sheet1": {
                    "iataCode": "TESTING",
                }
            }
            edit_sheety_row = requests.put(url=new_url, json=flight_codes)
        return edit_sheety_row

