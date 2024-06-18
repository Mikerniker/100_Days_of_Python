from bs4 import BeautifulSoup
import requests


response = requests.get("http://flavorsofcacao.com/database_w_REF.html")
chocolate_data = response.text


soup = BeautifulSoup(chocolate_data, "html.parser")

print(soup.title)

# from selenium import webdriver

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=chrome_options)