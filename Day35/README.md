# Day 35: Rain Alert App

## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [What I learned](#what-i-learned)

## Overview

### The challenge

- Build an app that alerts you when it is raining.

### Links

- Solution URL: [Rain Alert App](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day35)

## My process

- The original requirement was to send a message via Twilio, but I switched to Telegram to send a message. The code was also modified to send a sticker with a rain cloud to practice sending messages via the Telegram bot and to practice reading documentation. This was a bit challenging for me as I had a hard time figuring out how to send messages via Telegram via the documentation, especially when finding the chat_ids and understanding how the bot can send messages to the user. It took a while for me to figure out, but I was able to apply some of the concepts I learned from the previous modules to the Telegram documentation and some Googling.    

### Built with

- Python
- [OpenWeather API](https://openweathermap.org/api/one-call-api)
- [Latitude and Longitude Finder](https://www.latlong.net/)
- [Telegram API docs](https://core.telegram.org/bots/api)


### What I learned
- API: API Keys, Authentication
- Environment Variables
- Sending SMS via Telegram
- Review python slicing
- Tools: [JSON Viewer](http://jsonviewer.stack.hu/)