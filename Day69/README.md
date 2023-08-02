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