# Day 98 Professional Portfolio Project: Bitcoin Alert Bot for Telegram

## Overview
- Topics: Python and Telegram 

### The challenge

- Automate some aspect of your life using what you have learnt. This could be an aspect of your job, your schoolwork, your home, your chores. 
- Chose to make a **Bitcoin Alert Bot for Telegram Version**

A Bitcoin price alert bot for Telegram that monitors Bitcoin prices and sends notifications when your target prices are reached.

### Functionality

A Telegram bot that lets users track Bitcoin price movements and set custom alerts.  
It fetches live data from the [CoinGecko API](https://www.coingecko.com/) and notifies users when BTC crosses their chosen thresholds.

## Bot Commands

- `/start` - Welcome message and introduction
- `/help` - Show help information
- `/price` - Get current Bitcoin price
- `/alert` - Set a price alert (Above/Below threshold)
- `/my_alerts` - View your current alerts
- `/cancel` - Cancel any ongoing operation 

### Links

- Solution URL: [Bitcoin Alert Bot for Telegram](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day98)

## Reflection
**Approach, Challenges, Learnings, and Future Improvements:**


**Approach**
For this project, I explored the Telegram Bot documentation and tried to integrate parts of the sample code provided there. I also used AI-assisted tools like Claude and Cursor to help me structure and generate some of the code. My main goal was to learn how APIs, async programming, and the Telegram bot framework fit together.

**Challenges**
One of the biggest challenges was understanding the AI-generated code. Even though the AI could produce working snippets, I had to prompt it many times, test, and then adjust the output to make it function properly. Another challenge was mixing my own learning with the AI output, making sure I wasn’t just copying, but actually understanding what was happening in the program.

**Learnings**
This project gave me a chance to review core Python concepts and see new ones I hadn’t worked with before, like async functions, ConversationHandler, and threading. I also reviewed how to interact with external APIs (CoinGecko and Telegram Bot API). More importantly, I practiced using AI tools not as a shortcut, but as a way to guide and support my own learning.

**Future Improvements**
I know there’s still a lot I don’t fully understand in the code and still need to review and practice further. For the future steps or development, it would be useful to:

- Add persistence using a database instead of in-memory storage.
- Rely more on asyncio instead of mixing in threads.
- Deploy the bot to a server so I can test it in real-world conditions.
- Try extending it beyond Bitcoin, maybe supporting multiple cryptocurrencies.

## Notes/Concepts/Review: 

- [Telegram Docs](https://core.telegram.org/bots/samples)