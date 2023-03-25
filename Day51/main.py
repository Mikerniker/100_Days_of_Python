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
        self.service = Service(executable_path=CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service)


    def get_driver(self):
        service = Service(executable_path=self.chrome_driver_path)
        driver = webdriver.Chrome(service=service)
        return driver

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        go_button = self.driver.find_element(By.CLASS_NAME, "js-start-test")
        go_button.click()

        time.sleep(90)

        results = self.driver.find_elements(By.CLASS_NAME, "result-data")
    
        self.download = results[3].text
        self.upload = results[4].text
        print(f"download: {results[3].text} \nupload: {results[4].text}")
       



    def tweet_at_provider(self):
        pass


test = InternetSpeedTwitterBot()
driver = test.get_driver()
driver.get("https://twitter.com/home")

time.sleep(50)
