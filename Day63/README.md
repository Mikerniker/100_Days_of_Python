# Day 63 Virtual Bookshelf

https://github.com/Mikerniker/100_Days_of_Python/assets/63586831/c1bf6596-d1af-45ac-9b4c-5e004306706f

## Overview

- Topics: Flask, SQLite Databases (SQLite3; SQLAlchemy), CRUD Operations with SQLAlchemy

### The challenge

- Create an SQLite database for a Virtual Bookshelf and create, read, update and delete data in the database, connect it with a Flask app to serve data.


## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [Notes](#notes)

### Links

- Solution URL: [Virtual Bookshelf](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day63)

### Built with
- Flask
- HTML
- SQL 
- Python

### Notes
- Note 1: you got an error because you forgot to put book_id in the edit.html form action like you did in the index.html function.
- Note 2: You were initially confused if you could put a delete function with the home function but wrote a separate function for delete which worked out.
- Note 3: Angela's code used an input hidden option in her edit_rating.html
```<input hidden="hidden" name="id" value="{{book.id}}"> ```
- This field lets web developers include data that cannot be seen or modified by users when a form is submitted. A hidden field often stores what database record that needs to be updated when the form is submitted. [HTML <input type="hidden"> Source](https://www.w3schools.com/tags/att_input_type_hidden.asp#:~:text=The%20%3Cinput%20type%3D%22hidden,when%20the%20form%20is%20submitted.) I did not use this in my code but will use this as future reference.

### References:
- [SQL COMMANDS](https://www.codecademy.com/article/sql-commands)
- [SQL Create Table](https://www.w3schools.com/sql/sql_ref_create_table.asp)
