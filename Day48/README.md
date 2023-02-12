Day 48 Project: Cookie Game Playing Bot

## Overview

## Exercise 1 (main.py):
- Extract the upcoming event data from the python.org website. 
- Use Selenium to scrape all upcoming event date and event names andstore them in a nested Python dictionary. 
- Print the dictionary to the console. 
- The event data from python .org should be stored under the keys 'time; and 'name"

## Cookie Challenge (cookie.py)
- Access cookie to click
- Get product ids
- After 5 seconds check most affordable products to upgrade with cookie money and purchase the most expensive product
- After 5 minutes have passed since starting the game, stop the bot and print the "cookies/second".

## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [What I learned](#what-i-learned)



### Links

- Solution URL: [Cookie Game Playing Bot](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day48)

### Built with

- Python
- Selenium

### What I reviewed
- Scraping the Web with Selenium


#### Resources
- [XPath Turotiral](https://www.w3schools.com/xml/xpath_intro.asp)
- [Selenium Documentation](https://selenium-python.readthedocs.io/)

#### Notes
Exercise 1
- I realize that this solution is not the most efficient. I had a hard time figuring out how  to simplify it, but ended up with a longer than necessary solution. On the bright side, it works...

Cookie Game Challenge
- Had a really hard time figuring this out and had to eventually peek. I got some sections right but got confused with the time.time() reference, it was easier to follow after reading Angela's code.
- I had to also review the ```range(len(some_list))``` which was helped by this [reference](https://v4.software-carpentry.org/python/lists.html#:~:text=Well%2C%20if%20len(list),legal%20indices%20of%20the%20list.)
- I also had to review the get_attribute() element method in selenium. See this [reference](https://www.geeksforgeeks.org/get_attribute-element-method-selenium-python/)
