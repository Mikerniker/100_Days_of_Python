## IN PROGRESS

## Day 46 Project: Spotify Playlist Musical Time Machine

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
- [Spotify](https://developer.spotify.com/dashboard/)


### What I reviewed
- Scraping the Web with Beautiful Soup
- strip() method
- list comprehensions
- requests module

#### Notes
- I had a hard time figuring out the proper syntax for selectors, I was making the mistake of writing them separately (i.e. with spaces): ```selector: li h3 .c-title```  or ```selector: li hr c-title```, eventually saw an example for the right syntax: ```selector: li h3.c-title```  (i.e. no space between h3 and c-title with a . in between)
- Still To Figure out:
  - I initially was using find_all method, and couldn't figure out why this wasn't working: ```song_titles = soup.find_all(name="li h3")```, so I'm not so clear on why select works and not find_all for this exercise.
- I also found an alternative solution that worked, based on what I saw from [stackoverflow](https://stackoverflow.com/questions/35465182/how-to-find-all-divs-whose-class-starts-with-a-string-in-beautifulsoup): ```song_titles = soup.select("li h3[class*=c-title]")``` The original example: ```soup.select("div[class*=span3]")``` where # with *= means: contains. Though I'm not entirely clear on how this syntax works and I couldn't find it in the documentation. It also feels more accidental that I was able to modify the stackoverflow suggestion to find a suitable alternative solution. Will need to review this again at a later time.
- Notes for Step 2: I was stuck a bit because I had a hard time understanding the spotipy documentation. I realized a bit later that my mistake was adding quotation marks to the constants. My code seemed to work, but it was a bit different from Angela's version.
- Notes for Step 3:  Got stuck here too. The instructions for step 3 were a bit confusing, it took me a while to realize that the task was to use the "search method" (in spotipy) to look for uri's in Spotify, instead of making the uri's as some kind of string (i.e. f"spotify:track:"+ {song_name}") with a list comprehension. Took a bit of time on this, because I made some typos in the query (i.e. I used a "=" instead of ":"), which I didn't see initially...but was eventually able to figure it out after some time. I also had a hard time reading the results, since I could not get pprint to work so I had to manually go through each dictionary/list from the results printed out..which is not efficient I know...but hopefully will get there with more practice. 
- Notes for Step 4: I was able to complete step four more easily than the other steps, I just took time looking for the id's that were necessary for the user_id and the playlist_id which I manually looked for through the JSON files (which I know - is not efficient...so still need to work on using pprint for this). One other recurring issue I have is the need to keep refreshing tokens when they expire. I don't fully understand why Angela's code doesn't need to refresh the token. I know that the method class she uses saves it as a .txt file, but I don't really understand why mine doesn't seem to do the same so I will have to revisit this again to figure that part out. For now, I'm happy I was able to complete the exercise myself. For now, it's not as clean as Angela's, but I will work on that. 