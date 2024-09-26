from bs4 import BeautifulSoup
import requests
import pandas as pd
import json

response = requests.get("http://flavorsofcacao.com/database_w_REF.html")
chocolate_data = response.text

soup = BeautifulSoup(chocolate_data, "html.parser")

tables = soup.select(selector="#choco_database")
print(tables)

table = soup.find_all('table')[0]

#Get table titles
table_titles = table.find_all('th')
col_table_title = [title.text.strip() for title in table_titles]
df = pd.DataFrame(columns=col_table_title)

# Get table data
table_data = table.find_all('tr')

for row in table_data[1:]:
    row_data = row.find_all('td')
    cleaned_data = [data.text.strip() for data in row_data]
    length = len(df)
    df.loc[length] = cleaned_data

search_word = "Philippines"

# Find rows that contain the search word in country of origin
matching_rows = df[df["Country of Bean Origin"] == search_word]

# Convert the matching rows to JSON
chocolate_json_str = matching_rows.to_json(orient='records')

chocolate_json = json.loads(chocolate_json_str) 

print(chocolate_json)

# SHEETY SECTION
SHEETY_ENDPOINT_API = 'add_endpoint_here';

for item in chocolate_json:
    chocolate_data = {
        "sheet1": {
            "ref": item["REF"],  # No need for chocolate_json[item], item is already a dictionary
            "manufacturer": item["Company (Manufacturer)"],
            "companyLocation": item["Company Location"],
            "reviewDate":  item["Review Date"],
            "countryOrigin": item["Country of Bean Origin"],
            "barname": item["Specific Bean Origin or Bar Name"],
            "cocoaPercent": item["Cocoa Percent"],
            "ingredients": item["Ingredients"],
            "characteristics": item["Most Memorable Characteristics"],
            "rating": item["Rating"],
        }
    }

    sheet_response = requests.post(SHEETY_ENDPOINT_API, json=chocolate_data)
    print(sheet_response.status_code)
    print(sheet_response.text)