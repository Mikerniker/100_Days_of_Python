import requests
from pprint import pprint

#Get sheety data

SHEETY_URL = '#insertsheetyurl'

sheety_table = requests.get(SHEETY_URL)

sheety_table.raise_for_status()
sheet_data = sheety_table.json()['sheet1']
pprint(sheet_data)

all_prices = [item['lowestPrice'] for item in sheet_data]
print(all_prices)



