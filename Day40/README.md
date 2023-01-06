## Day 40 CAPSTONE: Part 2 - Cheap Flight Finder

## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [What I learned](#what-i-learned)

## Overview

### The challenge

- Step 1 - Create the Customer Acquisition Code
- Step 2 - Exception Handling for Destinations without Flights
  - when no flights are available add exception handling to code so it doesn't break.
- Step 3 - Destinations without Direct Flights
  - check for flights with one stop and notify user.
- Step 4 - Email all customers to notify them.

### Links

- Solution URL: [Cheap Flight Finder](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day40)

## Notes
- I kept getting an UnboundLocalError so I moved around my code in flight_search.py function: 
```def search_cheap_flights(self, depart_city, arrival_city, stopovers):```
 I ended up moving the print statement and the return statement within the try block.

- After trying to fix that, an AttributeError appeared in main.py, to resolve this I added it in another if-else block...which was not the cleanest after comparing it to Angela's code...so far it works.

- Part of the challenge was to see if there are flights with 1 stop if a flight is not found. The suggestion was to test this with LON to Bali, however no flights were found with this either. The forums also mentioned that there were limitations to API services of Kiwi. So I changed the search to look for two stops, which seemed to work. I need a code review though because it feels like my code is messy.

- I wasn't so clear on how Angela added/connected the customer acquisition task, so I just added it as a separate file (customers.py).

- The final code I made was pretty messy so I still need to review and figure out how to simplify it further. But I'm happy I got everything to "work."

### Built with

- Python
- [Kiwi Partners Flight Search API](https://partners.kiwi.com/)
- [Tequila Flight Search API](https://tequila.kiwi.com/portal/login)
- [Sheety API](https://sheety.co/)
- [Telegram API docs](https://core.telegram.org/bots/api)

### What I learned
- APIs and making POST Requests
- Python DateTime strftime()
- Timedelta in datetime module
- To fix the unicode encode error:
```
a.encode('utf-8')
```

### References
- [Python Continue Keyword](https://www.w3schools.com/python/ref_keyword_continue.asp)
- [UnboundLocalError](https://pythoncircle.com/post/680/solving-python-error-unboundlocalerror-local-variable-x-referenced-before-assignment/)
- [UnicodeEncodeError](https://stackoverflow.com/questions/9942594/unicodeencodeerror-ascii-codec-cant-encode-character-u-xa0-in-position-20#answer-9942885)