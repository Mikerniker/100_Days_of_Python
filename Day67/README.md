# Day 67 Blog Capstone Part 3: Building a RESTful Blog with Editing

## Overview

- Topics:  SQLAlchemy, WTForms, Datetime module, Jinja Templating

### The challenge

1. GET Blog post items
2. POST new blog posts
3. Edit existing blog posts
4. ELETE blog posts

### Links

- Solution URL: [Blog Capstone Part 3](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day67)

### Built with

- Python
- MySQL 
- SQLAlchemy
- WTForms

### References
- [WTForms support](https://pythonhosted.org/Flask-Bootstrap/forms.html)
- [CKEditor](https://flask-ckeditor.readthedocs.io/en/latest/basic.html)
- [Button Map](https://pythonhosted.org/Flask-Bootstrap/forms.html#form-macro-reference) - used to change the color of the button on wtf form
- [Jinja Safe Filter](https://jinja.palletsprojects.com/en/2.11.x/templates/#safe)
example: ```e.g. {‌{ Jinja expression | Jinja filter }}```   ```e.g. {‌{ {{post.body | safe }} }}```