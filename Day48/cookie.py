#IN PROGRESS

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


chrome_driver_path = "D:\DEVELOPMENT\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")

countdown = 50
while countdown > 0:
    cookie.click()
    countdown -= 1

cookie_money = driver.find_element_by_id("money")
print(cookie_money.text)
print(type(cookie_money.text))


cursor_price = driver.find_element_by_css_selector("#buyCursor b")
cursor_words = cursor_price.text
price = int(cursor_words.split(" ")[2])
print(price)

#TEST

def get_price(selector):
    price = driver.find_element_by_id(selector)
    return price

def format_price(count):
    cookie_count = count.text
    try:
        cookie_number = cookie_count.split(" ")[2].split("\n")[0].replace(',', '')
        # print(f"{selector}: {cookie_number}")
        return int(cookie_number)
    except ValueError:
        cookie_number = cookie_count.split(" ")[3].split("\n")[0].replace(',', '')
        # print(f"{selector}: {cookie_number}")
        return int(cookie_number)


cursor = int(get_price("buyCursor"))
grandma = int(get_price("buyGrandma"))
factory = int(get_price("buyFactory"))
mine = int(get_price("buyMine"))
shipment = int(get_price("buyShipment"))
alchemy = int(get_price_alternate("buyAlchemy lab"))
portal = int(get_price("buyPortal"))
time_machine = int(get_price_alternate("buyTime machine"))


print(grandma)
print(factory)
print(mine)
print(shipment)
print(alchemy)
print(portal)
print(time_machine)

#COOKIES PERSECOND
cookies_per_second = driver.find_element_by_id("cps")
print(f"C per C: {cookies_per_second.text}")