#IN PROGRESS

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
- Step 4: Currently in progress...


### Built with

- Python
- [Kiwi Partners Flight Search API](https://partners.kiwi.com/)
- [Tequila Flight Search API](https://tequila.kiwi.com/portal/login)
- [Sheety API](https://sheety.co/)

### What I learned
- APIs and making POST Requests
- Python DateTime strftime()
- Authorization Headers (Basic Authentication)
- Environment Variables
