# Day 69: Blog Capstone Project Part 4: Adding Users

## Overview

- Topics: 

### The challenge

 

### Links

- Solution URL: [Blog Capstone Project Part 4: Adding Users](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day69)

### Built with

- Python
- Flask


### References

- [One to Many relationship SQL](https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html#one-to-many)
- [SQL Basic Relationship Patterns](https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html)

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
3. 