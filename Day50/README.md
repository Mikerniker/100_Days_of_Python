# Day 50 Project: Auto Tinder Swiping Bot

## Overview

### The challenge

## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [What I learned](#what-i-learned)

### Links

- Solution URL: [Tinder Swiper](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day50)

### Built with

- Python
- Selenium

### What I reviewed
- Scraping Tinder with Selenium

#### Resources

#### Notes

- You received an error "DeprecationWarning: executable_path has been deprecated"
You found this resource: https://bobbyhadz.com/blog/python-deprecationwarning-executable-path-has-been-deprecated
And changed some parts of the code to :
```
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
```
You installed selenium and webdriver
And you changed the chrome drive path to this:
```
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://www.python.org")
```
You also had to follow the new documentation and changed this:
```
log_in = driver.find_element_by_class_name("l17p5q9z")
```
to this:
```
log_in = driver.find_elements(By.CLASS_NAME, "c1p6lbu0")
```
You have to use these new methods:
https://bobbyhadz.com/blog/python-deprecationwarning-executable-path-has-been-deprecated#deprecationwarning-find_element_by_-commands-are-deprecated

Another option to connect to webdriver from another tutorial:
```
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://tinder.com/")
```
From this YT video https://www.youtube.com/watch?v=NJTNeXofbps

- Notes 3/18/2022, some helpful tutorials that helped me bypass the chrome bot detection
1. I imported ```import undetected_chromedriver as uc``` to replace ```from selenium import webdriver```
2. after activating my venv I: pip install undetected-chromedriver
3. The original tutorial I watched was from [xtekky](https://www.youtube.com/watch?v=GcTGurNyf6Y) on youTube. I had to refer to the original documentation on by [ultrafunkamsterdam's github](https://github.com/ultrafunkamsterdam/undetected-chromedriver/blob/master/README.md#important-note) and used this:
```
import undetected_chromedriver as uc
driver = uc.Chrome()
``` which worked until the point at which I was asked for two-factor authentication, which I will have to temporarily remove for easier testing.
- Notes 3/19 Just got banned from Tinder for following Angela's instructions. Note the intention was to swipe to not match with anyone and to delete the account after since it was mainly for this project. Currently looking for an alternative project. 
- 3/20/2023 Alternative project is to try this with OkCupid instead, since they also have a desktop option. Currently was able to access site and used selenium to login with username and password. 
- 3/22/2023 The final version is simpler than Angela's, one because the HTML code of OkCupid is easier to read and navigate compared to Tinder. Tinder also seems to be a lot [stricter in identifying bots](https://www.wired.com/story/dating-apps-tools-to-thwart-scams/). For the alternate exercise I just opted to log in and pass on the first 10 people, I used 10 because I was worried the bot would be detected and I didn't want to hurt people's feelings with a fake account. One major limitation with my code is that it doesn't catch the required OTP that is sent to your phone in order to login. The only ways I could find to address this is either having a Twilio account or if the OTP was sent via email. However, OkCupid doesn't seem to allow the OTP to be sent via email and I currently cannot use Twilio. So the OTP has to be manually added during time.sleep. 