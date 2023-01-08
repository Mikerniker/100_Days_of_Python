## Day 45 Project: Scrape a List of 100 Greatest Movies

## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [What I learned](#what-i-learned)

## Overview

### The challenge

- Create a .txt file after scraping the Top 100 movies (starting from 1) from the Empire website.

### Links

- Solution URL: [Scrape a List of 100 Greatest Movies](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day45)

## Notes


### Built with

- Python
- [Empire Magazine](https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/)


### What I learned
- Scraping the Web with Beautiful Soup

#### Notes
- Had to resolve a unicode error with a writelines section, I found two options for that:
  - 1. Add ```.encode("UTF-8"))``` example ```f.write(s.encode("UTF-8"))```
  - 2. Adding encoding to the with open section:
```
with open("movies.txt", "w", encoding="utf-8") as file:
    for title in titles:
        file.writelines(f"{title}\n")
```
- The second option worked better for me. See [reference](https://stackoverflow.com/questions/5483423/how-to-write-unicode-strings-into-a-file)
- To reverse the list of movies, I used the .reverse() method. Angela also gave examples of other options:
  - To use slice reverse [::-1]
  - And the for loop option:
  ```
  for n in range(len(movie_titles) - 1, -1, -1):
      print(movie_titles[n])
  ```  