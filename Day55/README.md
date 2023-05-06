# Day 55 HTML & URL Parsing in Flask and the Higher Lower Game

## Overview

- Advanced Decorators, Rendering HTML, Parsing URLs and Flask Debugging

### The challenge

- Recreate the higher lower game using Flask, Create a route that can detect the number entered by the user and checks that number against a generated random number between 0 and 9. If the number is too low, tell the user it's too low, same with too high or if they found the correct number. Try to make the h1 text a different colour for each page. 

## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [Notes](#notes)

### Links

- Solution URL: [Flask and the Higher Lower Game](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day55)

### Built with

- Python
- Flask


#### Notes
Topics:
- Flask URL Paths and the Flask Debugger
- Rendering HTML Elements with Flask
- Use Python Decorators to Style HTML Tags
- Decorators with *args and **kwargs

Other Notes
- Debugging: Had some initial difficulties with "Not Found The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again." - This happened because the site was still running on the previous server so (on Windows) you had to do a ctrl+alt+delete to restart everything. Then the code started working properly.
