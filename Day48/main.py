#Exercise 1 
#Challenge: Use Selenium to Scrape Website Data

from selenium import webdriver
chrome_driver_path = "D:\DEVELOPMENT\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.python.org/")

get_dates = driver.find_elements_by_css_selector(".event-widget ul.menu time")

dates = []
for date in get_dates:
    dates.append(date.text)
#print(dates)

get_events = driver.find_elements_by_css_selector(".event-widget ul.menu a")
events =[]
for event in get_events:
    events.append(event.text)
#print(events)

merged_list = list(zip(dates, events))
merged_events = list(enumerate(merged_list))

numbered_events = {x:y for (x, y) in merged_events}

new_dict = {}
for keys, value in numbered_events.values():
    new_dict['time'] = keys
    new_dict['name'] = value

for event in numbered_events.keys():
    numbered_events[event] = new_dict
print(numbered_events)

driver.quit()