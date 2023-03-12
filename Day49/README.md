# Day 49 Project: Automated Job Applications with Selenium

## Overview

### The challenge

- Step 1 Setup LinkedIn
- Step 2 Automatically Login
- Step 3 Apply for a Job
  - Use Selenium to apply to first job that only requires a phone number
  - Alternative: Use Selenium to save (all) jobs(s) and follow the company that posted the listing(s).
- Step 4 Apply for all the jobs
  - If applying for a job:
    - Apply to standard, 1-step applications
    - Ignore applications that require a note
    - Ignore complex, multi-step applications
  - Else, just save the job and follow the company.

For the project, I opted to just save and follow the jobs that had the following conditions: the job had a 1-step application and ignore complex, multi-step applications.
At the time of doing this project, the option to ignore applications that require a note was not possible as the available jobs on LinkedIn did not have the option to write notes, so I could not identify the appropriate element for this.


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
- [Scrolling with Selenium and Python](https://riptutorial.com/selenium-webdriver/example/28140/scrolling-using-python)
- [Scrolling to Element](https://intellipaat.com/community/30985/python-selenium-scroll-to-element-scrolling-to-element-using-webdriver) - This resource is what helped me figure out how to finally move down the screen.


#### Notes

- For Step 3, my code was a little different from Angelas, I added an option to save the new page which you're redirected to after clicking on a button. This was achieved by window_handles and switch_to_window. i.e.
```
linkedin_signin_window = driver.window_handles[0]
print(linkedin_signin_window)

linkedin = driver.switch_to.window(linkedin_signin_window)
```
I'm not sure if I understood this part correctly. In Angela's code she doesn't use this but uses time.sleep(5) to wait for the new page to load (I added this later on for other steps).

- Spent several days trying to resolve the ElementClickInterceptedException that appears when trying to click on the follow button. Came across several stack overflow and other resources to help me resolve it. While I understand what is causing the error, and have identified it, I can't seem to figure out how to make it switch to the desired button. So far, I have tried using ActionChains and move_to_element, [scroll_into_view](https://stackoverflow.com/questions/41744368/scrolling-to-element-using-webdriver), [switch_to_active_element](https://www.selenium.dev/selenium/docs/api/py/webdriver_remote/selenium.webdriver.remote.switch_to.html), and also tried accessing the section where the follow button was to see if it will enable access to the follow button, but that didn't work either. Since I spent too long trying to figure this out, will leave it for now and resolve it with a try and except option and come back to it in a future time -- hopefully when I understand selenium better.

- [aria label reference](https://stackoverflow.com/questions/58734107/typeerror-webelement-object-is-not-subscriptable) Came across this other error: TypError: 'WebElement' object is not subsriptable, which I found means "implies that you have attached an index to a WebElement which is not supported"
- After so long I finally figured out how to click the buttons I couldn't click. The steps I used to resolve it was first to maximize the window using ```driver.maximize_window()```, then I closed all overlaying buttons (i.e. the pop up message that appears when saving a job, and the messaging bar on the right) as these intercepted attempts to click on the buttons. Then I used action chains to move to the bottom of the page to access the follow button. 

- Other things I learned: when using Actions chains I originally tried moving the screen to the section where the Follow button was :
```
locate_follow_section = driver.find_element_by_css_selector(".jobs-company__box")
action = ActionChains(driver)
action.move_to_element(locate_follow_section)
```
This didn't work because the messaging section was still overlaying / intercepting any clicks to the follow button. To work around that, I had to access something even lower, so changed it to the area near the footer so the screen would scroll down even more to make the follow button visible. This seemed to work:
```
locate_follow_section = driver.find_element_by_css_selector(".jobs-company__footer")
actions = ActionChains(driver)
actions.move_to_element(locate_follow_section).perform()
```
One error that I might have made was that the .perform() was not included in the first attempt, so that may have also been why it initially didn't work.

- Another thing I opted to do was to use other css labels or attributes to dismiss a popup. Originally, I used the class name: 
```dismiss_button = driver.find_element_by_class_name("artdeco-modal__confirm-dialog-btn")```
which works, but I wanted to try using "data-control-name" and "aria labels", which seemed more readable and so I could remember what I was looking for. This is what I used for the dismiss button:
```dismiss_button = driver.find_element(By.CSS_SELECTOR, '[data-control-name="discard_application_confirm_btn"]')```
and this is what I used to find the Submit Application button with an aria label:
```find_submit_application = driver.find_element(By.CSS_SELECTOR, '[aria-label="Submit application"]')```
Not entirely sure if this is the right way to go, but I found it more helpful in remembering what I was trying to do.
