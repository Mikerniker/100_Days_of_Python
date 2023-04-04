from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.common.keys import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = "D:\DEVELOPMENT\chromedriver.exe"
TWITTER_EMAIL = "************"
TWITTER_PASSWORD = "************"
TWITTER_USERNAME = "************"
GOOGLE_PASSWORD = "*************"

class InternetSpeedTwitterBot:

    def __init__(self):
        self.promised_down = PROMISED_DOWN
        self.promised_up = PROMISED_UP
        self.service = Service(executable_path=CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")

        go_button = self.driver.find_element(By.CLASS_NAME, "js-start-test")
        go_button.click()

        time.sleep(70)
        results = self.driver.find_elements(By.CLASS_NAME, "result-data")
    
        self.download = results[3].text
        self.upload = results[4].text
        return f"Hey Internet Provider, why is my internet speed {self.download} down/{self.upload} up " \
               f"when I pay for {self.promised_down} down/{self.promised_up} up?"

    def twitter_login(self, email): 
        self.driver.get("https://twitter.com")

        time.sleep(35)

        login_button = self.driver.find_element(By.CSS_SELECTOR, '[href="/login"]')

        login_button.click()
        time.sleep(5)

        twitter_signin_popup = self.driver.window_handles[0]
        self.driver.switch_to.window(twitter_signin_popup)

        time.sleep(3)
        login = self.driver.find_element(By.NAME, "text")
        login.send_keys(email)
        # print(login.text)
        next_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]")
        next_button.click()

        time.sleep(10)

    def tweet_at_provider(self, password, message):
            password_input = self.driver.find_element(By.NAME, "password")
            password_input.send_keys(password)

            next_button2 = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div")
            next_button2.click()

            time.sleep(15)

            tweet = self.driver.find_element(By.CSS_SELECTOR, '[aria-label="Tweet"]')
            tweet.click()

            time.sleep(5)

            write_tweet = self.driver.find_element(By.CLASS_NAME, "public-DraftStyleDefault-ltr")
            write_tweet.send_keys(message)

            tweet_button = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="tweetButton"]')
            tweet_button.click()

    def unusual_login(self, twitter_user):
            unusual_login_alert = self.driver.find_element(By.NAME, "text")
            unusual_login_alert.send_keys(twitter_user)
            unusual_login_alert.send_keys(Keys.ENTER)

post_tweet = InternetSpeedTwitterBot()
tweet_message = post_tweet.get_internet_speed()
post_tweet.twitter_login(TWITTER_EMAIL)

try:
    post_tweet.tweet_at_provider(TWITTER_PASSWORD, tweet_message)
except NoSuchElementException:
    post_tweet.unusual_login(TWITTER_USERNAME)
    time.sleep(6)
    post_tweet.tweet_at_provider(TWITTER_PASSWORD, tweet_message)

time.sleep(50)
