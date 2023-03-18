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
