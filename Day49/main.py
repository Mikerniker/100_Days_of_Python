from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

MY_EMAIL = "********************"
MY_PASSWORD = "*****************"

chrome_driver_path = "D:\DEVELOPMENT\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3362855988&f_AL=true&f_WT=2&geoId=103121230&keywords=python%20developer&location=Philippines&refresh=true")
driver.maximize_window()

sign_in_webpage = driver.find_element_by_link_text("Sign in")
sign_in_webpage.click()

linkedin_signin_window = driver.window_handles[0]

linkedin = driver.switch_to.window(linkedin_signin_window)
username = driver.find_element_by_id("username")
username.send_keys(MY_EMAIL)

password = driver.find_element_by_id("password")
password.send_keys(MY_PASSWORD)

signin_button = driver.find_element_by_class_name("btn__primary--large")
signin_button.click()

time.sleep(5)

# Save and Follow all the clickable jobs that only have one step
all_jobs = driver.find_elements_by_css_selector(".job-card-container--clickable")
for job in all_jobs:
    job.click()
    time.sleep(3)

    # Click on Easy apply
    find_easy_apply = driver.find_element_by_class_name("jobs-apply-button--top-card")
    find_easy_apply.click()
    close_easyapp_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
   
    try:
        find_submit_application = driver.find_element(By.CSS_SELECTOR, '[aria-label="Submit application"]')

        if find_submit_application:
            close_easyapp_button.click()
            time.sleep(2)
            dismiss_button = driver.find_element(By.CSS_SELECTOR, '[data-control-name="discard_application_confirm_btn"]')
            dismiss_button.click()

            #Save the job
            time.sleep(2)
            save_button = driver.find_element_by_class_name("jobs-save-button")
            save_button.click()

            time.sleep(5)

            # Close pop up that say the job has been saved 
            close_popup = driver.find_element_by_css_selector(".artdeco-toast-item__dismiss")
            close_popup.click()

            # Click on Follow Button
            locate_follow_section = driver.find_element_by_css_selector(".jobs-company__footer")

            actions = ActionChains(driver)
            actions.move_to_element(locate_follow_section).perform()

            time.sleep(2)

            get_follow_button = driver.find_element_by_css_selector(".follow")
            get_follow_button.click()

    except NoSuchElementException:
        find_next_button = driver.find_element(By.CSS_SELECTOR, '[aria-label="Continue to next step"]')
        print(find_next_button.text)
        print("There are too many steps to this application. Don't save and skip to next job.")
        close_easyapp_button.click()
        time.sleep(2)
        dismiss_button = driver.find_element(By.CSS_SELECTOR, '[data-control-name="discard_application_confirm_btn"]')
        dismiss_button.click()
