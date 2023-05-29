# Day 60 POST Requests with Flask and HTML Forms

## Overview

- POST requests with Flask, HTML Forms, send emails with smtplib

### The challenge

- HTML Forms -Revision - Creating a Form from Scratch
- Handle POST Requests with Flask Servers
- Get the Contact Form from Day 59 to work
- Sending Emails with SMTPLIB

Tasks
- Add a route in main.py to receive data from the form from Day 59
- Update the code in contact.html and main.py so that the information the user has entered into the form and return a <h1> that says "Successfully sent your message".
- Combine the "/contact" route with "/form-entry" so that they are both under the route "/contact" but depending on which method (GET/POST) that triggered the route, handle it appropriately.
- Instead of returning a <h1> that says "Successfully sent message", update the contact.html file so that the <h1> on the contact.html file becomes "Successfully sent message".
- Send form contents as an email using smtplib.

## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [Notes](#notes)

### Links

- Solution URL: [POST Requests with Flask and HTML Forms](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day60)

### Built with
- Flask
- HTML


### Notes
- Had a hard time returning an <h1> that says "Successfully sent message", update the contact.html file so that the <h1> on the contact.html file becomes "Successfully sent message". using the Jinja docs, had to check Angelas guide since I was stuck on this particular task for a while. 
This is the final code in contact.html:
```
                         {% if msg_sent: %}
                                <h1>Successfully sent your message.</>
                                {% else %}
                                <h1>Contact Me</h1>
                                {% endif %}
```
And msg_sent was added to the route in main:
```
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        send_email(name, email, phone, message)
        return render_template("contact.html", msg_sent=True)
    else:
        return render_template("contact.html", msg_sent=False)

```