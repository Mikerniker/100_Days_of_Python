## IN PROGRESS

## Day 45 Project: Spotify Playlist Musical Time Machine

## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [What I learned](#what-i-learned)

## Overview

### The challenge

- Step 1: Scrape the Billboard Hot 100.
- Step 2: Authenticate with Spotify
- Step 3: Search Spotify for the Songs from Step 1
- Step 4: Create and Add to Spotify Playlist

### Links

- Solution URL: [Spotify Playlist Musical Time Machine](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day46)

### Built with

- Python
- [Billboard 100](https://www.billboard.com/charts/hot-100/2000-08-12/)


### What I reviewed
- Scraping the Web with Beautiful Soup

#### Notes
- I had a hard time figuring out the proper syntax for selectors, I was making the mistake of writing them separately (i.e. with spaces): ```selector: li h3 .c-title```  or ```selector: li hr c-title```, eventually saw an example for the right syntax: ```selector: li h3.c-title```  (i.e. no space between h3 and c-title with a . in between)
- Still To Figure out:
  - I initially was using find_all method, and couldn't figure out why this wasn't working: ```song_titles = soup.find_all(name="li h3")```, so I'm not so clear on why select works and not find_all for this exercise.
- I also found an alternative solution that worked, based on what I saw from [stackoverflow](https://stackoverflow.com/questions/35465182/how-to-find-all-divs-whose-class-starts-with-a-string-in-beautifulsoup): ```song_titles = soup.select("li h3[class*=c-title]")``` The original example: ```soup.select("div[class*=span3]")``` where # with *= means: contains. Though I'm not so clear on how this syntax works compared and I couldn't find it in the documentation.