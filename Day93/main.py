from bs4 import BeautifulSoup
import requests
import pandas as pd

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

# Search for data relevant to Philippines
search_word = 'Philippines'
