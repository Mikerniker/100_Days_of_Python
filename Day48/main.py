#TESTING;  NOT THE FINAL CODE
#Challenge: Use Selenium to Scrape Website Data
#Extract the upcoming event data from the python.org website. Use Selenium to scape all upcoming event date and event names andstore them in a nested Python dictionary. Print the dictionary to the console. The event data from python .org should be stored under the keys 'time; and 'name"

from selenium import webdriver

chrome_driver_path = "D:\DEVELOPMENT\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")


get_dates = driver.find_elements_by_css_selector(".event-widget ul.menu time")

dates = []
for date in get_dates:
    dates.append(date.text)

print(dates)

get_events = driver.find_elements_by_css_selector(".event-widget ul.menu a")
events =[]
for event in get_events:
    events.append(event.text)
print(events)


merged_list = list(zip(dates, events))
print(merged_list)
merged_events = list(enumerate(merged_list))
print(merged_events)



driver.quit()