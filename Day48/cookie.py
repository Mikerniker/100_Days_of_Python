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
    price = driver.find_element_by_css_selector(f"#{selector}")
    words = price.text
    cookie_number = words.split(" ")[2].split("\n")[0]
    # print(f"{selector}: {cookie_number}")
    return cookie_number
