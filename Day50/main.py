from selenium import webdriver
import time

chrome_driver_path = "D:\DEVELOPMENT\chromedriver.exe"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://tinder.com/")


time.sleep(3)

log_in = driver.find_elements_by_class_name("c1p6lbu0")

for item in log_in:
    if item.text == "Log in":
        item.click()

time.sleep(10)
