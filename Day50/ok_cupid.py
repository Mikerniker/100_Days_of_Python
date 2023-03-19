from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

MY_EMAIL = "*********************"
MY_PASSWORD = "*************"

chrome_driver_path = "D:\DEVELOPMENT\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.okcupid.com/")
wait = WebDriverWait(driver, 10)
driver.maximize_window()
