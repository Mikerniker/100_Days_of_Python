from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

#requests allows us to get hold of the data from a particular url
zillow = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.64481581640625%2C%22east%22%3A-122.22184218359375%2C%22south%22%3A37.64220115428586%2C%22north%22%3A37.908142595089714%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
CHROME_DRIVER_PATH = "D:\DEVELOPMENT\chromedriver.exe"

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding":"gzip, deflate, br",
    "upgrade-insecure-requests":"1"
}

response = requests.get(zillow, headers=headers)
zillow_page = response.text

print(zillow_page)

soup = BeautifulSoup(zillow_page, "html.parser")

all_sites = soup.find_all(name="a")
print(all_sites)

# properties = soup.find_all("div", {"class": "search-page-container"})

#Links to the property
links = soup.find_all("a", {"class": "property-card-link"})
# print(links)

all_property_links = [link.get("href") for link in links]
new_property_links = ["https://www.zillow.com" + link for link in all_property_links if "https://www.zillow.com" not in link]

#GET PRICES
all_prices = soup.find_all("div", {"class": "StyledPropertyCardDataArea-c11n-8-85-1__sc-yipmu-0"})
print(all_prices)

price_list = [item.text for price in all_prices for item in price.find_all('span')]
# print(price_list)

prices = [price.replace('/', '+').split('+')[0] for price in price_list] 
# print(prices)

# GET ADDDRESS
find_addresses = soup.find_all(name="address")
addresses = [adds.text for adds in find_addresses]
print(addresses)

#SELENIUM
service = Service(executable_path=CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdgf9wgrDe1E_GtfgL1NdfM-VQhL6bw1Md_qS3-T3lxELCLSA/viewform?usp=sf_link")

for item in range(2):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdgf9wgrDe1E_GtfgL1NdfM-VQhL6bw1Md_qS3-T3lxELCLSA/viewform?usp=sf_link")

    time.sleep(5)
    all_fields = driver.find_elements(By.CLASS_NAME, "whsOnd.zHQkBf")
    # all_fields = driver.find_element(By.XPATH, "/html/body/div/div[3]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    # print(all_fields)
    for item in all_fields:
        item.send_keys("attempt1")