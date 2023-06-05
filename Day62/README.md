# Day 62 Coffee and Wifi Project: Advanced Flask, WTForms, Bootstrap, and CSV

## Overview


### The challenge


## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [Notes](#notes)

### Links

- Solution URL: [Coffee and Wifi Project](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day62)

### Built with
- Flask
- HTML
- Bootstrap
- CSV

### Notes
- Note 1: Had to add ```encoding="utf8"```
```
    with open('cafe-data.csv', newline='', encoding="utf8") as csv_file:
```
to fix errors reading the file
- Note 2: Couldn't figure out why my Flask debugger wasn't working, finally found 
```$env:FLASK_DEBUG = "1"``` to type in my Windows power shell, which fixed the issue.
- Note 3: Added Redirect AND Url_For which wasn't in the original instructions
```from flask import Flask, render_template, redirect, url_for```
For use in the app route:
```
@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("cafe-data.csv", mode="a") as csv_file:
            csv_file.write(f"\n{form.cafe.data},"
                           f"{form.location.data},"
                           f"{form.open.data},"
                           f"{form.close.data},"
                           f"{form.coffee_rating.data},"
                           f"{form.wifi_rating.data},"
                           f"{form.power_rating.data}")
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)
```
