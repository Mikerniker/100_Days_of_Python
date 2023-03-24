from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

CHROME_DRIVER_PATH = "D:\DEVELOPMENT\chromedriver.exe"

service = Service(executable_path=CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)

driver.get("https://www.speedtest.net/")

go_button = driver.find_element(By.CLASS_NAME, "js-start-test")
go_button.click()
