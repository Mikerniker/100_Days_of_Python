from bs4 import BeautifulSoup
import requests


amazon_url = "https://www.amazon.com/Instant-Pot-Pressure-Steamer-Sterilizer/dp/B08PQ2KWHS/ref=sr_1_5?crid=1HBIPQA988RCO&keywords=instant+pot+duo+evo&qid=1673901445&s=home-garden&sprefix=instant+pot+%2Cgarden%2C2424&sr=1-5"

amazon_headers = {
    "Accept-Language":"en-US,en;q=0.9,fil;q=0.8,fr;q=0.7",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
}

response = requests.get(amazon_url, headers=amazon_headers)
product_page = response.text
# print(product_page)

soup = BeautifulSoup(product_page, "lxml")

product_price = soup.find(name="span", class_="a-price")

price = product_price.getText().split("$")
print(f"$ {price[1]}")