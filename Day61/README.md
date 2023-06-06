# Day 61 Advanced Forms with Flask-WTForms

## Overview

- Build forms using the Flask-WTF extension for Flask

### The challenge

TASKS
- Install Flask-WTF
- Create forms with Flask-WTF
- Add Validation to Forms with Flask-WTF
- Inherit Templates using Jinja2
- Use Flask-Bootstrap as an Inherited Template


## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [Notes](#notes)

### Links

- Solution URL: [Advanced Forms with Flask-WTForms](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day61)

### Built with
- Flask
- HTML
- Bootstrap


### Notes

- Always use dynamically built urls:
```<form method="POST" action="{{ url_for('login') }}">```

- WTF Basic Fields (StringField, PasswordField, SubmitField etc)
- [WTF Basic Fields](https://wtforms.readthedocs.io/en/3.0.x/fields/#basic-fields)