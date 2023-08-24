# Day 71: Deploying the Web Application

## Overview

- Topics: Flask, Web Hosting (Render), .gitignore, Version Control, Environment Variables, Gunicorn, PostgreSQL

[Live Site](https://my-adventure-blog.onrender.com/)

### Tasks

- Add a .gitignore file 
- Use git to add version control to project
- Use environment variables to store sensitive information
- Set up a WSGI server with gunicorn
- Push to remote on Github
- Host on web service provider
- Upgrade SQLite Database to PostgreSQL


### Links

- Solution URL: [Deploying the Web Application](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day71)

### Built with


### References
- [Gunicorn](https://gunicorn.org/)
- [Psycopg2-binary](https://pypi.org/project/psycopg2-binary/)


### Notes
1. To Enable Version Control Integration in PyCharm
- In the PyCharm GUI go to VCS -> Enable Version Control Integration. (equivalent to typing git init in the Terminal)
2. [WSGI aka Web Server Gateway Interface](https://www.python.org/dev/peps/pep-3333/) 
- normal web servers can't run Python applications, so a WSGI is a special type of server to run Flask app. A WSGI server standardises the language and protocols between the Python Flask application and the host server. The most popular WSGI server is - gunicorn, but there are others.
3.  SQLite vs PostgreSQL
SQLite
- is a file-based database.
- Strength is it's useful to see how the data looks using DB Viewer while coding up the database and debugging. 
- Weakness: once it's deployed with a hosting provider (like Render) the file locations are shifted around every 24 hours so the database might just get wiped every day.
PostgreSQL
- a database that can handle millions of data entries and reliably delivers data to users

4. When pasting internal database URL as the key value (for deployment). The first part of the URL should be changed from postgres to postgresql. The URI has to start with "postgresql" because this is required by SQLAlchemy. The reason we can seamlessly switch from SQLite to Postgres during deployment on (Render) is because we use the psycopg package in combination with SQLAlchemy.