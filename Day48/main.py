#TESTING;  NOT THE FINAL CODE
#Challenge: Use Selenium to Scrape Website Data
#Extract the upcoming event data from the python.org website. Use Selenium to scape all upcoming event date and event names andstore them in a nested Python dictionary. Print the dictionary to the console. The event data from python .org should be stored under the keys 'time; and 'name"

from selenium import webdriver

chrome_driver_path = "D:\DEVELOPMENT\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")


find_the_thing = driver.find_elements_by_css_selector(".event-widget ul.menu time")

dates = []
for i in find_the_thing:
    dates.append(i.text)

print(dates)

event_names = driver.find_elements_by_css_selector(".event-widget ul.menu a")
events =[]
for a in event_names:
    events.append(a.text)
print(events)

all_things = driver.find_elements_by_css_selector(".event-widget ul.menu")

for all in all_things:
    print(all.text)


driver.quit()