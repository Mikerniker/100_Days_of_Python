# Day 53 CAPSTONE Project: Data Entry Job Automation

## Overview

### The challenge
- Use Beautiful soup to find the addresses, prices, and links to home listings
- Use Selenium to add the data into a Google form to be used in a spreadsheet

## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [Notes](#notes)

### Links

- Solution URL: [Data Entry Job Automation](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day53)

### Built with

- Python
- Selenium
- Beautiful Soup


#### Notes
- 4/21/2023 added headers because Zillow checks if you're a bot with captcha. So added the following section to bypass the captcha: 
```
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding":"gzip, deflate, br",
    "upgrade-insecure-requests":"1"
}

response = requests.get(zillow, headers=headers)
```
Reference for headers: [Source 1](https://morioh.com/p/e23b427aabde) [Source 2](https://www.scrapingdog.com/blog/scrape-zillow/)
- 4/23/2023 Had to find a resource on how to split a string with multiple characters. Found some different options such as the re method ```import re``` but opted to use 
the str.replace() method to replace the first delimiter with the second, then using the str.split() mthod to split the string. [Source 1](https://bobbyhadz.com/blog/python-split-string-multiple-delimiters)
- Found a resource on how to get a span using Beautiful soup and ended up using ```price.find_all('span')``` [Source](https://pytutorial.com/find-span-element-python-beautifulsoup/)
- 4/24/2023 Was a bit confused on how to make a list comprehension for a double for loop. Was able to figure it out after a while. This resource helped [Source](https://stackoverflow.com/questions/1198777/double-iteration-in-list-comprehension). the code was shortened from this:
```
price_list = []
for price in all_prices:
    all_spans = price.find_all('span')
    for item in all_spans:
        price_list.append(item.text)
```
to this:
```
price_list = [item.text for price in all_prices for item in price.find_all('span')]
```
Also shortened this:
```
prices = []
for thing in price_list:
    new_list = thing.replace('/', '+').split('+')
    prices.append(new_list[0])
```
to
```
prices = [price.replace('/', '+').split('+')[0] for price in price_list]  
```
Take me a while to make though, it also feels like I made it less readable. But will just use this as practice for list comprehensions.