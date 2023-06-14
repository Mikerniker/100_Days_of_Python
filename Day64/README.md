# Day 64 Top 10 Movies Website

## Overview

- Topics: Flask, SQLite Databases (SQLite3; SQLAlchemy), CRUD Operations with SQLAlchemy

### The challenge

- 

## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [Notes](#notes)

### Links

- Solution URL: [Top 10 Movies Website](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day64)

### Built with
- Flask
- HTML
- SQL 
- Python

### Notes
- NOTE 1 6/15/2023: You got a "METHOD not Allowed error because you did not put
``` methods=["GET", "POST"] ``` to your decorator: 
```
@app.route('/add', methods=["GET", "POST"])
def add_movie():
```


### References: