## Day 39 CAPSTONE: Part 1 - Cheap Flight Finder


## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [What I learned](#what-i-learned)

## Overview

### The challenge

- Find flight deals via an API. Use Google sheets to keep track of the locations you want to visit with a price cutoff. Take the data from Google sheet and feed it into the Flight Search API that will look for the cheapest flights within the next 6 months and send an alert/SMS to your mobile phone.

### Links

- Solution URL: [Cheap Flight Finder](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day39)

## Notes
- I did this a few months ago but am re-doing it again now because I had a lot of difficulties with this challenge. It's still difficult and is taking me longer than usual as I need to remember and review some of the concepts I learned from the past lectures.  
- I finally finished Step 3 of the challenge (as given by Angela) and this was particularly difficult, I spent a few days trying to figure out how to get the iata code and print it on the sheet via the Classes. Without using classes the tasks seemed a bit easier, but putting them in separate modules and figuring out how to make them interact with each other confused me for several days. I also did some indentation errors, which sometimes still take me a while to figure out. 
- The added pressure also comes from the limited usage I'm allowed from the Sheety API to test my code. Progressing through each task is taking a while but I'm slowly getting there. 12/30/2022
- Mental Note: Be careful with your indentations in your functions/methods.
- Step 4: 
- Mental Note: Don't forget to reassign your variables when you make changes and need to access them again like for strftime, save it instead of printing it.
- January 1: added methods to flight_search, modified main, and added flight data module.
- Mental Notes: I still get confused on when running a for loop when only the last or the first get printed out on some occasions, and I found this helpful note on [reddit](https://www.reddit.com/r/learnpython/comments/tc32uw/why_is_my_loop_only_iterating_once/): "Any function will run the return statement only once. As soon as it encounters return, the function will end. Hence, a function can only return one output. And you can't return from a for loop, return will only work with a function. So even if it's inside a for loop, it will return from the function and the loop will end after the first iteration. Usually when you want to return multiple values from a function, you have to add all those values to a list or tuple and return the list after the iterations have completed." so I ended up changing my search_cheap_flights(self, sheety) method to return a list of dictionaries instead to see the results I wanted.
Finished January 2: The last few steps really confused me especially when trying to connect the different modules with each other. I finally had to peek to see how they were connected. For the most part, I saw that a lot of the code I made had similarities to the final solution, I had to make changes as I originally kept the for loop within the function to make requests to the Tequila app, whereas Angela's code kept them separate. This is where I got stuck for a few days. I ended up following Angela's code of keeping them separate which made things a lot easier to figure out. My code is not as clean as hers but it gets the overall action done. Will work on making it cleaner in the future. Currently, I'm happy that I finally got it to work.  
- Other Notes: The code was working when I started getting an index error, which was confusing because I didn't change anything to the original code - which was working. So I was able to use a Try and Except option, which helped with the index error issue. 
- Also, Angela's original code uses Twilio, this was modified to use Telegram instead. 

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
- OOP Classes
- Exception Handling

### References
- [Timedelta Reference 1](https://www.geeksforgeeks.org/python-find-yesterdays-todays-and-tomorrows-date/)
- [Timedelta Reference 2](https://stackoverflow.com/questions/4541629/how-to-create-a-datetime-equal-to-15-minutes-ago/4541668)