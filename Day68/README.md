# Day 68

## Overview

- Topics: Flask 

### The challenge

- 

### Links

- Solution URL: [Authentication](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day68)

### Built with

- Python

### References
- [flask.send__from_directory](https://flask.palletsprojects.com/en/2.3.x/api/#flask.send_from_directory)
- [generate_password_hash](https://werkzeug.palletsprojects.com/en/2.3.x/utils/#module-werkzeug.security)


### Notes

- 07/26/2023 I was trying to find what the difference in output between request.form and request.form.get is since the output remains the same,  currently it seems they do the same thing just with a different syntax ``` name = request.form['name']``` vs ```name=request.form.get('name')```. Can't seem to find a clear reference explaining the differences between the two for posts requests. [Reference 1](https://code.luasoftware.com/tutorials/flask/flask-get-request-parameters-get-post-and-json)