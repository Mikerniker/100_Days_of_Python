from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "D:\DEVELOPMENT\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3362855988&f_AL=true&f_WT=2&geoId=103121230&keywords=python%20developer&location=Philippines&refresh=true")

sign_in_webpage = driver.find_element_by_link_text("Sign in")
sign_in_webpage.click()

linkedin_signin_window = driver.window_handles[0]
print(linkedin_signin_window)