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
5. Note to self: You got a bit confused when creating the One to Many Relationships for BlogPost,
User, and Comment

Because you're forgetful, this is to remind your future self about what you did for Parent-Child Relationship between BlogPost and User:

  - For BlogPost Class (the CHILD), you created a Foreign Key, where "user.id" --> 'user' refers to the tablename of User. You also created a reference to the User object (author), where "posts" refers to the posts property in the User class.
```
    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    author = relationship("User", back_populates="posts")
```

  - For User Class (the PARENT), you created "posts" which will act like a List of BlogPost objects attached to each User. The "author" refers to the author property in the BlogPost class you created.
```posts = relationship("BlogPost", back_populates="author")```

Similarly, this is what you did for Parent-Child Relationship between Comment and User:     

  - For the User Class (the PARENT), you created "comment", where "commenter" refers to the commenter property in the Comment class.

```comment = relationship("Comment", back_populates="commenter")```

  - For Comment Class (the CHILD), you created a Foreign Key, where "user.id" --> 'user' refers to the tablename of User. You also created a reference to the User object (commenter), where "comment" refers to the comment property in the User class.

```
author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
commenter = relationship("User", back_populates="comment")
```
- Finally, you also created a One to Many Relationship between Blogpost and Comment

  - BlogPost (the PARENT), you created post_comments where "blog_commenter" refers to the blog_commenter property in the Comment class.
```
post_comments = relationship("Comment", back_populates="blog_commenter")
```
  - Comment Class (the CHILD), you created a Foreign Key, where "blog_posts.id" --> 'blog_posts' refers to the tablename of BlogPost. You also created a reference to the BlogPost object (blog_commenter), where "post_comments" refers to the post_comments property in the BlogPost class.

```
blog_id = db.Column(db.Integer, db.ForeignKey("blog_posts.id"))
blog_commenter = relationship("BlogPost", back_populates="post_comments")
```


