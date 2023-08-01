# Day 68: Authentication with Flask

## Overview

- Topics: Authentication, Encryption and Hashing, Salting Passwords, Hashing and Salting using Wekzeug, Flask-Login, Flask Flash Messages Passing Authentication Status to Templates (Template Inheritance) 

### The challenge

1. Register new users to a database, and greet them when registered
2. Hash and salt user's passwords using Werkzeug
3. Authenticating users with Flask-Login, limit access if they aren't logged in
4. Use Flask Messages to give user feedback on their actions (Topics reviewed: conditionals)
5. Use Template Inheritance to hide/show login/register buttons to Users
 

### Links

- Solution URL: [Authentication with Flask](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day68)

### Built with

- Python
- Flask


### References
- [flask.send__from_directory](https://flask.palletsprojects.com/en/2.3.x/api/#flask.send_from_directory)
- [generate_password_hash](https://werkzeug.palletsprojects.com/en/2.3.x/utils/#module-werkzeug.security)
- [Flask Message Flashing](https://flask.palletsprojects.com/en/2.3.x/patterns/flashing/)
- [UserMixin](https://www.thedigitalcatonline.com/blog/2020/03/27/mixin-classes-in-python/)
- [check_password_hash(pwhash, password)](https://werkzeug.palletsprojects.com/en/2.3.x/utils/#werkzeug.security.check_password_hash)
- [Flask-Login Documentation](https://flask-login.readthedocs.io/en/latest/)

### Notes

- 07/26/2023 I was trying to find what the difference in output between request.form and request.form.get is since the output remains the same,  currently it seems they do the same thing just with a different syntax ``` name = request.form['name']``` vs ```name=request.form.get('name')```. Can't seem to find a clear reference explaining the differences between the two for posts requests. [Reference 1](https://code.luasoftware.com/tutorials/flask/flask-get-request-parameters-get-post-and-json)
- 08/02/2023 The Angelas code had
```
@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)
```    
 "db.get_or_404()", which is a new function for me. Reference from flask-sqlalchemy describes "get_or_404(ident, description=None) as: Like get() but aborts with 404 if not found instead of returning None." [Reference 1](https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/)

2. Another new function ```check_password_hash()```
```werkzeug.check_password_hash(pwhash, password)[source]```
Definition: This checks a password against a given salted and hashed password value. In order to support unsalted legacy passwords this method supports plain text passwords, md5 and sha1 hashes (both salted and unsalted). Returns True if the password matched, False otherwise. From: [Reference 2](https://tedboy.github.io/flask/generated/werkzeug.check_password_hash.html)
