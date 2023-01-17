## Day 47 Project: Amazon Price Tracker

## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [What I learned](#what-i-learned)

## Overview

### The challenge

- Step 1: Use BeautifulSoup to Scrape the Product Price
- Step 2: Email Alert When Price Below Preset Value

### Links

- Solution URL: [Amazon Price Tracker Project](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day47)

### Built with

- Python
- [Amazon](https://www.amazon.com/Instant-Pot-Pressure-Steamer-Sterilizer/dp/B08PQ2KWHS/ref=sr_1_5?crid=1HBIPQA988RCO&keywords=instant%2Bpot%2Bduo%2Bevo&qid=1673901445&s=home-garden&sprefix=instant%2Bpot%2B%2Cgarden%2C2424&sr=1-5&th=1)


### What I reviewed
- Scraping the Web with Beautiful Soup
- smtplib module
- requests module


#### Notes
- This was easier than the task on Day46 was able to do the steps without much difficulty. I had to do some minor error handling with the UnicodeEncodeError which I was able to resolve by adding .encode() at the end of the email message: ```msg=f"Subject:Amazon Price alert! \n\n{message}.".encode("UTF-8")```
 