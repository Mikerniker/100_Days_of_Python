# Day 94 Professional Portfolio Project: Automate the Google Dinosaur Game

https://github.com/user-attachments/assets/16b0eac4-1dd0-46b0-99c6-be8d25453528

(Video is sped up)

## Overview

- Topics: pyautogui, python, PIL

### The challenge

- Write Python code to play the [Google Dinosaur Game](https://elgoog.im/t-rex/).
 
### Links

- Solution URL: [Custom Web Scraper](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day94)

## Reflection
**Approach, Challenges, Learnings, and Future Improvements:** 
Approach
- Started by locating the dinosaur to initialize the game.
- Identified the positions of relevant images for game elements.
- Defined a detection zone to trigger the dinosaur's jump.

## Notes: 
- When starting, raise ImageNotFoundException sometimes happens for `locate_dinosaur` but refreshing the page works. 
Future fixes:
1. Code doesn't work when it shifts to night mode
2. Enhance functionality so the dinosaur can duck under overhead obstacles. Dinosaur currently doesn't duck when overhead pterodactyl appears though it doesn't appear necessary since the pterodactyl doesn't touch the dinosaurs head.
3. Future fix could account for game speed changes and night mode transition.


## References
