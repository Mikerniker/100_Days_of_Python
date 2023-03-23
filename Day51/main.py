from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "D:\DEVELOPMENT\chromedriver.exe"
TWITTER_EMAIL = "milqueecode@gmail.com"
TWITTER_PASSWORD = "@ng3l@Pyth0n"

class InternetSpeedTwitterBot:

    def __init__(self):
        self.promised_down = PROMISED_DOWN
        self.promised_up = PROMISED_UP
        self.chrome_driver_path = CHROME_DRIVER_PATH

    def get_driver(self):
        service = Service(executable_path=self.chrome_driver_path)
        driver = webdriver.Chrome(service=service)
        return driver

    def get_internet_speed(self):
        pass

    def tweet_at_provider(self):
        pass


test = InternetSpeedTwitterBot()
driver = test.get_driver()
driver.get("https://twitter.com/home")

time.sleep(50)
