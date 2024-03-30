# In PROGRESS 


# Day 89 Professional Portfolio Project: ToDo App


## Overview

- Topics: Python, Flask, SQLAlchemy, REST APIs, Auth, Web Development  

### The challenge

- Build a ToDo app.

### Links

- Solution URL: [To Do List](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day89)

## Reflection
**Approach & Challenges:** 

**Biggest learning:**

**Future Improvements:**

## Notes:
- To fix the database error and connect the user to their respective todos, you had to fix your get_all _todos to query to the current user then you had to add the owner to the saved database in the  mytodo function: 
 ```
 owner_id=current_user.id,
            owner=current_user,
            ```
- Keep getting the documentation for flask-bootstrap and bootstrap-flask confused, mental note: this is the documentation I use for bootstrap 5 so as not to get confused:
[Bootstrap-Flask](https://bootstrap-flask.readthedocs.io/en/stable/migrate/) 
- For Bootstrap 4 & 5
- Make bootstrap container rounded at rounded-number [Rounded container](https://mdbootstrap.com/learn/mdb-foundations/bootstrap/rounded-corners/#:~:text=In%20Bootstrap%2C%20it's%20very%20easy,class%20rounded%2D4%20or%20similar.)
- To format jinja strftime example: ```{{ todo["start_time"].strftime('%H:%M') }}```

## References:
- [Contenteditable Reference](https://www.w3schools.com/tags/att_global_contenteditable.asp)
- To fix sizing and alignment with [render_field](https://bootstrap-flask.readthedocs.io/en/stable/macros/#render_field)  with              
- ```{{ render_field(form.email, form_type="horizontal", horizontal_columns=('lg', 2, 8)) }}```
- ```form_type="horizontal"``` aligns the label with the input
- ```horizontal_columns=('lg', 2, 8)``` allows the size of the column size of the label (2) and input (8) to be adjusted
