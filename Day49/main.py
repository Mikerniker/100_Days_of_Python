from selenium import webdriver
from selenium.webdriver.common.keys import Keys

MY_EMAIL = "********************"
MY_PASSWORD = "*****************"

chrome_driver_path = "D:\DEVELOPMENT\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3362855988&f_AL=true&f_WT=2&geoId=103121230&keywords=python%20developer&location=Philippines&refresh=true")

sign_in_webpage = driver.find_element_by_link_text("Sign in")
sign_in_webpage.click()

linkedin_signin_window = driver.window_handles[0]
print(linkedin_signin_window)

linkedin = driver.switch_to.window(linkedin_signin_window)
username = driver.find_element_by_id("username")
username.send_keys(MY_EMAIL)

password = driver.find_element_by_id("password")
password.send_keys(MY_PASSWORD)

signin_button = driver.find_element_by_class_name("btn__primary--large")
signin_button.click()

time.sleep(6)

find_save = driver.find_element_by_class_name("jobs-save-button")
find_save.click()


# TESTING FOR FOLLOW BUTTON
#This button is intercepting my access to follow button
intercepting_button = driver.find_elements_by_css_selector(".msg-overlay-bubble-header__control--new-convo-btn")
intercepting_button[1].click()




#TESTING THIS
# all_jobs = driver.find_elements_by_css_selector(".job-card-list div a")
#
# # print(all_jobs)
# for job in all_jobs:
#     print(job.text)

#TEST

list_jobs = driver.find_elements_by_css_selector(".job-card-container")
all_jobs = [job.text for job in list_jobs]
print(all_jobs)

#TEST 2
time.sleep(5)
apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
apply_button.click()

#test 3 this works

phone = driver.find_element_by_class_name("artdeco-text-input--input")
#thisworks
phone = driver.find_element_by_id("single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-3362855988-75565821-phoneNumber-nationalNumber")
# phone = driver.find_element_by_class_name("fb-single-line-text__input")
if phone.text == "":
    phone.send_keys("test")