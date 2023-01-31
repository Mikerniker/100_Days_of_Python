from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "D:\DEVELOPMENT\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")

countdown = 50
while countdown > 0:
    cookie.click()
    countdown -= 1