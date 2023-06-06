# Day 62 Coffee and Wifi Project: Advanced Flask, WTForms, Bootstrap, and CSV

## Overview


### The challenge

TASKS
- Add css using jinja 
- Make sure routes are correct 
- Make a Bootstrap table which shows all the data from the cafe-data.csv
- Location URL should be rendered as an anchor tag and should have the link text "Maps Link" and the href should be the actual link.
- Buttons and navigations links should function and lead to correct pages 
-  Use WTForms to create a quick_form in the add.html page
- Use validators
- Append added data via add.html to the csv file

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
to fix Unicode errors reading the file
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
- Note 4: To add a link to the table I added:
```<li><a href="{{ href }}">{{ caption }}</a></li>```
- Note 5: Had difficulties figuring out how to not add "Maps Link" text to the first row for "Location" had to check after a while. Just needed another for loop.
- Note 6: Initially got confused what item[0:4] referred to (i.e. list index or the string index) in Angela's code but slowly realized it referred to the string index and the reason I got errors in showing the "Map Link" text was because there was an extra space in the csv file I created when appending new cafes.
```
  {% for cafe in cafes: %}
          <tr>
            {% for item in cafe %}
            {% if item[0:4] == "http" %}
            <td><a href="{{ item }}">Maps Link</a></td>
```            
I had to remove the space after the comma in ```new_data = f"\n{form.cafe.data},{form.location.data},``` in main.py

References:

- [Bootstrap blocks](https://pythonhosted.org/Flask-Bootstrap/basic-usage.html#templates)
- [Super Blocks](https://pythonhosted.org/Flask-Bootstrap/basic-usage.html#examples)
- [WTF Forms Flask Bootstrap](https://pythonhosted.org/Flask-Bootstrap/forms.html)
- [WTF Validators](https://wtforms.readthedocs.io/en/2.3.x/validators/)
- [Disable Client Side Validation](https://stackoverflow.com/questions/41300647/wtforms-disable-client-side-validation-on-cancel/61166621#61166621)
- [Write Files](https://www.w3schools.com/python/python_file_write.asp)