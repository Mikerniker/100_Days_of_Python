import requests
from pprint import pprint

#Get sheety data

SHEETY_URL = '#insertsheetyurl'

sheety_data = requests.get(SHEETY_URL)

sheety_data.raise_for_status()
data = sheety_data.json()['sheet1']
pprint(data)

all_prices = [item['lowestPrice'] for item in data]
print(all_prices)