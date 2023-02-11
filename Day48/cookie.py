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

#5 seconds from now
five_seconds = time.time() + 5

# 5 minutes from now
five_minutes = time.time() + 60*5


while True:
    cookie.click()
    if time.time() > five_seconds:
        product_prices = []
        products = driver.find_elements_by_css_selector("#store b")
        for product in products:
            price = (product.text.split("-")[-1].replace(',', '').strip())
            if price != '':
                product_prices.append(int(price))
        print(product_prices)

        # Get cookie money
        find_cookie_money = driver.find_element_by_id("money")
        cookie_money = int(find_cookie_money.text.replace(',', ''))
        print(cookie_money)

        product_catalogue = {}
        for item in range(len(product_prices)):
            product_catalogue[all_products[item]] = product_prices[item]
        print(product_catalogue)
        print(product_catalogue.items())

        # Get items that can be upgraded
        can_upgrade = {}
        for id, price in product_catalogue.items():
            if price < cookie_money:
                can_upgrade[id] = price
        print(can_upgrade)

        most_expensive_item = max(can_upgrade)
        print(most_expensive_item)

        buy_upgrade = driver.find_element_by_id(most_expensive_item)
        buy_upgrade.click()

        five_seconds = time.time() + 5

    if time.time() > five_minutes:
        # Get cookies per second
        cookies_per_second = driver.find_element_by_id("cps")
        print(f"Cookies per second: {cookies_per_second.text}")

        break