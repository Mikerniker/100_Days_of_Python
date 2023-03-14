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