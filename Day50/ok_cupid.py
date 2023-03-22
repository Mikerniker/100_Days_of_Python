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

# SIGN INTO OK CUPID
time.sleep(3)
sign_in = driver.find_element(By.CLASS_NAME, "c0J0grIjyKY6YuiL9OO7")
sign_in.click()

time.sleep(10)

username = driver.find_element(By.NAME, "username")
username.send_keys(MY_EMAIL)

password = driver.find_element(By.NAME, "password")
password.send_keys(MY_PASSWORD)

next_button = driver.find_element(By.CLASS_NAME, "login-actions-button")
next_button.click()


time.sleep(160)

"""
During this time a OTP password is sent, which at the time of this posting,
can only be done manually before the rest of the code continues
"""

pass_button = driver.find_element(By.CSS_SELECTOR, '[aria-label="Pass and view the next profile"]')

for i in range(10):
    pass_button.click()
    time.sleep(3)
