# IN PROGRESS
# Day 49 Project: Automated Job Applications with Selenium

## Overview


## Automated Job Applications with Selenium
- 

## Table of contents

- [Overview](#overview)
  - [The challenge](#the-challenge)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [What I learned](#what-i-learned)



### Links

- Solution URL: [Automated Job Applications with Selenium](https://github.com/Mikerniker/100_Days_of_Python/tree/main/Day49)

### Built with

- Python
- Selenium

### What I reviewed
- Scraping LinkedIn with Selenium


#### Resources

- [Selenium Documentation](https://selenium-python.readthedocs.io/)

#### Notes

- My code is a little different from Angelas, I added an option to save the new page which you're redirected to after clicking on a button. This was achieved by window_handles and switch_to_window. i.e.
```
linkedin_signin_window = driver.window_handles[0]
print(linkedin_signin_window)

linkedin = driver.switch_to.window(linkedin_signin_window)
```
I'm not sure if I understood this part correctly. In Angela's code she doesn't use this but uses time.sleep(5) to wait for the new page to load.