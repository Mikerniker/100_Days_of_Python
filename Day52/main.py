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
        pass
    
    def find_followers(self):
        pass
    
    def follow(self):
        pass