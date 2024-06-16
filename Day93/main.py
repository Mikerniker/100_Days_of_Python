from bs4 import BeatifulSoup
import requests

#requests allows us to get hold of the data from a particular url

response = requests.get("https://flavorsofcacao.com/chocolate_database.html")
chocolate_data = response.text

soup = BeautifulSoup(chocolate_data, "html.parser")

print(soup.title)

# from selenium import webdriver

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=chrome_options)