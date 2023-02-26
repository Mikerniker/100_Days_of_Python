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
- [Move to vs Scroll into view](https://stackoverflow.com/questions/34562095/scrollintoview-vs-movetoelement) - This resources explains the differences between move_to_element and scroll_into_view.
- [move_to_element method – Action Chains](https://www.geeksforgeeks.org/move_to_element-method-action-chains-in-selenium-python/)

#### Notes

- My code is a little different from Angelas, I added an option to save the new page which you're redirected to after clicking on a button. This was achieved by window_handles and switch_to_window. i.e.
```
linkedin_signin_window = driver.window_handles[0]
print(linkedin_signin_window)

linkedin = driver.switch_to.window(linkedin_signin_window)
```
I'm not sure if I understood this part correctly. In Angela's code she doesn't use this but uses time.sleep(5) to wait for the new page to load.

- Spent several days trying to resolve the ElementClickInterceptedException that appears when trying to click on the follow button. Came across several stack overflow and other resources to help me resolve it. While I understand what is causing the error, and have identified it, I can't seem to figure out how to make it switch to the desired button. So far, I have tried using ActionChains and move_to_element, [scroll_into_view](https://stackoverflow.com/questions/41744368/scrolling-to-element-using-webdriver), [switch_to_active_element](https://www.selenium.dev/selenium/docs/api/py/webdriver_remote/selenium.webdriver.remote.switch_to.html), and also tried accessing the section where the follow button was to see if it will enable access to the follow button, but that didn't work either. Since I spent too long trying to figure this out, will leave it for now and resolve it with a try and except option and come back to it in a future time hopefully when I understand selenium better.
