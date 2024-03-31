# Day 89 Professional Portfolio Project: ToDo App


## Overview

- Topics: Python, Flask, SQLAlchemy, REST APIs, Auth, Web Development  

### The challenge

- Build a ToDo app.

### Links

- Solution URL: [To Do List](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day89)

## Reflection
**Approach & Challenges:** 
I enjoyed the process of creating the interface and designing the website. One of the challenges I had was resolving a database error and establishing connections between users and their respective todo pages, as well as addressing issues related to sizing and alignment using ```render_field```.

**Biggest learning:**
During this project, I came across some new concepts. One was ```contenteditable``` for HTML, which I'm still trying to figure out how to use with Python. I'm still looking for resources to figure out how to  effectively store contenteditable items in the database.

**Future Improvements:**
There are several areas that can still be improved including, enhancing the UI and UX, implementing features such as enhanced interactivity and the ability for users to have collaborative pages for team work, integrating a calendar and enhancing security and authentication. I've decided to leave it as is for now, but hope to improve it later on.

## Notes and References::
- To fix the database error and connect the user to their respective todos, you had to fix your ```get_all _todos``` to query to the current user then you had to add the owner to the saved database in the  mytodo function: 
```
owner_id=current_user.id,
            owner=current_user,
```
- Keep getting the documentation for flask-bootstrap and bootstrap-flask confused, mental note: so as not to get confused, this is the documentation I use for bootstrap 4/ 5 :
[Bootstrap-Flask](https://bootstrap-flask.readthedocs.io/en/stable/migrate/) 
- To make bootstrap container rounded: [Rounded container](https://mdbootstrap.com/learn/mdb-foundations/bootstrap/rounded-corners/#:~:text=In%20Bootstrap%2C%20it's%20very%20easy,class%20rounded%2D4%20or%20similar.)
- To format jinja strftime example: ```{{ todo["start_time"].strftime('%H:%M') }}```
- [Content Editable Reference](https://www.w3schools.com/tags/att_global_contenteditable.asp)
- To fix sizing and alignment with [render_field](https://bootstrap-flask.readthedocs.io/en/stable/macros/#render_field) :              
- ```{{ render_field(form.email, form_type="horizontal", horizontal_columns=('lg', 2, 8)) }}```
- ```form_type="horizontal"``` aligns the label with the input
- ```horizontal_columns=('lg', 2, 8)``` allows the size of the column size of the label (2) and input (8) to be adjusted.
