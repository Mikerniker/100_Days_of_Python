from bs4 import BeautifulSoup
import requests


response = requests.get("http://flavorsofcacao.com/database_w_REF.html")
chocolate_data = response.text


soup = BeautifulSoup(chocolate_data, "html.parser")

tables = soup.select(selector="#choco_database")
print(tables)

# print(tables)

# table_titles = soup.findAll('table')[0].findAll('th')
# # print(table_titles)

# for title in table_titles:
#     print(title.getText())



table = soup.find_all('table')[0]

table_titles = table.find_all('th')
table_data = table.find_all('tr')

column_title = [title.getText() for title in table_titles]
column_data = [item.getText() for item in table_data]
print(column_data)
# from selenium import webdriver

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=chrome_options)