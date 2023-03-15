from selenium import webdriver
import time



service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://tinder.com/")
wait = WebDriverWait(driver, 20)

#ALTERNATIVE driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


time.sleep(3)

log_in = driver.find_elements_by_class_name("c1p6lbu0")

for item in log_in:
    if item.text == "Log in":
        item.click()

time.sleep(10)
