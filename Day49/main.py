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