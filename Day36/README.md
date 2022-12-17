# Day 36: Stock News Monitoring Project

## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [What I learned](#what-i-learned)

## Overview

### The challenge

- Step 1: Monitor when stock price increases/decreases by 5% between yesterday and the day before yesterday.
- Step 2: Get the first 3 news pieces for the COMPANY_NAME. 
- Step 3: Send a separate message with the percentage change and each article's title and description to your Telegram.  

##### Note:
- The original challenge was to send the message via Twilio, but Telegram was used for this instead.

### Links

- Solution URL: [Stock News Monitoring Project](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day36)

## My process
- Some differences between my code and Angela's code. I added additional parameters for the news, which may not have been necessary. I also used the datetime module instead of indexing the items on the list. I hope to simplify the code and make it cleaner in the future as I learn more. 

### Built with

- Python
- [Alpha Vantage API](https://www.alphavantage.co)
- [News API](https://newsapi.org)
- [Telegram API docs](https://core.telegram.org/bots/api)


### What I reviewed
- API: API Keys, Authentication
- Sending Messages via Telegram
- Tools: [JSON Viewer](http://jsonviewer.stack.hu/)