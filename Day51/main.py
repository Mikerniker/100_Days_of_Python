#Replace webdriver with this:
import undetected_chromedriver as uc
# from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "D:\DEVELOPMENT\chromedriver.exe"
TWITTER_EMAIL = "************"
TWITTER_PASSWORD = "************"
GOOGLE_PASSWORD = "*************"

class InternetSpeedTwitterBot:

    def __init__(self):
        self.promised_down = PROMISED_DOWN
        self.promised_up = PROMISED_UP
        self.service = Service(executable_path=CHROME_DRIVER_PATH)
        # self.driver = webdriver.Chrome(service=self.service)
        self.driver = uc.Chrome()  #Replaced above with this


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
        self.driver.get("https://twitter.com")

        time.sleep(40)

        login_button = self.driver.find_element(By.CSS_SELECTOR, '[href="/login"]')
        login_button.click()
        time.sleep(5)

        
        twitter_signin_popup = self.driver.window_handles[0]
        signin = self.driver.switch_to.window(twitter_signin_popup)

        time.sleep(3)
        sign_in_popup = self.driver.find_element(By.CLASS_NAME, "S9gUrf-YoZ4jf")
        sign_in_popup.click()

        google_popup = self.driver.window_handles[1]
        self.driver.switch_to.window(google_popup)

        google_username = self.driver.find_element(By.NAME, "identifier")
        google_username.send_keys(email)

        next_button = self.driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe-OWXEXe-k8QpJ")
        next_button.click()

        time.sleep(3)
        
        google_password = self.driver.find_element(By.NAME, "Passwd")
        google_password.send_keys(password)

        next_button = self.driver.find_element(By.CLASS_NAME, "VfPpkd-LgbsSe-OWXEXe-k8QpJ")
        next_button.click()


test = InternetSpeedTwitterBot()
# driver = test.get_driver()
# driver.get("https://twitter.com")
test.tweet_at_provider(TWITTER_EMAIL, GOOGLE_PASSWORD)

time.sleep(50)
