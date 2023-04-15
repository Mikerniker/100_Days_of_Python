from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys 
import time


CHROME_DRIVER_PATH = "D:\DEVELOPMENT\chromedriver.exe"
SIMILAR_ACCOUNT = "selfcareisforeveryone"
USERNAME = ""
PASSWORD = ""

class Instafollower:
    def __init__(self) -> None:
        self.service = Service(executable_path=CHROME_DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.service)


    def login(self):
        self.driver.get("https://www.instagram.com/")

        username = self.driver.find_element(By.NAME, "username")
        username.send_keys(USERNAME)

        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)

        time.sleep(10)
    
    def find_followers(self):
        self.driver.get("https://www.instagram.com/selfcareisforeveryone/")
        time.sleep(3)
        followers = self.driver.find_element(By.CSS_SELECTOR, '[href="/selfcareisforeveryone/followers/"]')
        followers.click()

        time.sleep(8)

        followers_popup = self.driver.window_handles[0]
        self.driver.switch_to.window(followers_popup)
        
        time.sleep(5)

    def follow(self):
        for i in range(5):
            follow_button = self.driver.find_elements(By.TAG_NAME, "button")
            for button in follow_button:
                button.click() 
                time.sleep(2)
            # Scroll down
            follower_names = self.driver.find_element(By.CLASS_NAME, "_aano")
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", follower_names)
            time.sleep(2)

        time.sleep(40)
    

instagram = Instafollower()
instagram.login()
instagram.find_followers()
instagram.follow()