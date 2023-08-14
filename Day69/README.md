# Day 69: Blog Capstone Project Part 4: Adding Users

## Overview

- Topics: Flask, SQL, Gravatar

### The challenge

 

### Links

- Solution URL: [Blog Capstone Project Part 4: Adding Users](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day69)

### Built with

- Python
- Flask
- SQL

### References

- [One to Many relationship SQL](https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html#one-to-many)
- [SQL Basic Relationship Patterns](https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html)
- [Flask-Gravatar](https://flask-gravatar.readthedocs.io/en/latest/)
- [Gravatar](https://en.gravatar.com/)

### Notes
- Notes 8/3/2023
1. wtf form in Bootstrap 5 is different
The following were added on register.html
```
{% from "bootstrap5/form.html" import render_form %}
```
and to main.py
```
<div class="col-lg-8 col-md-10 mx-auto">
  {{ render_form(form) }}
</div>
```
2. Reminder used  ```app.app_context().push()```

- Notes 8/9/2023
3. [Flask abort() function](https://flask.palletsprojects.com/en/2.3.x/api/#flask.abort) 
- when using abort in flask import it: ```from flask import abort```
- example ```abort(404)``` or ```abort(403)```

4. When creating a python decorator import: ```from functools import wraps```
- had some difficulties making the python decorator, this was my original code:
```
def admin_only(function):
    @wraps(function)
    def decorated_function(*args, **kwargs):
        if current_user.id == 1:
            return function(*args, **kwargs)
        else:
            return abort(403)
    return decorated_function
```
Angela's code is simpler/easier, used it instead for future reference
```
def admin_only(function):
    @wraps(function)
    def decorated_function(*args, **kwargs):
        # If id is not 1 then return abort with 403 error
        if current_user.id != 1:
            return abort(403)
        # Otherwise continue with the route function
        return function(*args, **kwargs)

    return decorated_function
```
5. Note to self: Add note here about one to many relationship when your brain is not fried.