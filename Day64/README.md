# Day 64 Top 10 Movies Website

## Overview

- Topics: Flask, SQLite Databases (SQLite3; SQLAlchemy), CRUD Operations with SQLAlchemy

### The challenge

- 

## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [Notes](#notes)

### Links

- Solution URL: [Top 10 Movies Website](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day64)

### Built with
- Flask
- HTML
- SQL 
- Python

### Notes
- NOTE 1 6/15/2023: You got a "METHOD not Allowed error because you did not put
``` methods=["GET", "POST"] ``` to your decorator: 
```
@app.route('/add', methods=["GET", "POST"])
def add_movie():
```
- NOTE 2 6/19/2023 Angelas code was a littl different, for the final home function task she used:
```
@app.route("/")
def home():
    #This line creates a list of all the movies sorted by rating
    all_movies = Movie.query.order_by(Movie.rating).all()
    
    #This line loops through all the movies
    for i in range(len(all_movies)):
        #This line gives each movie a new ranking reversed from their order in all_movies
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)
```
I used enumerate:
```
@app.route("/")
def home():
    all_movies = db.session.query(Movie).order_by(Movie.rating.desc())
    for index, movie_rank in enumerate(all_movies, 1):
        movie_rank.ranking = index
    db.session.commit()
    return render_template("index.html", movies=all_movies)
```


### References: