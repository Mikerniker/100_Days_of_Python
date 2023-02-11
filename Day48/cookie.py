
from selenium import webdriver
import time


chrome_driver_path = "D:\DEVELOPMENT\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Get cookie to click
cookie = driver.find_element_by_id("cookie")

# Get product ids
products = driver.find_elements_by_css_selector("#store div")
all_products = [product.get_attribute("id") for product in products]
print(all_products)

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



#TEST 2
products = driver.find_elements_by_css_selector("#store b")

product_prices = []
for product in products:
    price = (product.text.split("-")[-1].replace(',', '').strip())
    if price != '':
        product_prices.append(int(price))


print(product_prices)

can_afford = []
for price in product_prices:
    if price < cookie_money:
        can_afford.append(price)
print(can_afford)

product_to_buy = can_afford[-1]
index_of_item = can_afford.index(product_to_buy)
print(f"index of item is {index_of_item}")

products[index_of_item].click()


#COOKIES PERSECOND
cookies_per_second = driver.find_element_by_id("cps")
print(f"C per C: {cookies_per_second.text}")