# IN PROGRESS
# Day 53 CAPSTONE Project: Data Entry Job Automation

## Overview

### The challenge



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