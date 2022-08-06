from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = Service("C:\SeleniumDriver\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)

driver.get("https://www.python.org/")
upcoming_events_date = driver.find_elements(By.CSS_SELECTOR, '.blog-widget time')
upcoming_events_name = driver.find_elements(By.CSS_SELECTOR, '.blog-widget li a')
events ={}

for n in range(len(upcoming_events_date)):
    events[n] = {
        "time": upcoming_events_date[n].text,
        "name": upcoming_events_name[n].text
    }
print(events)




driver.close()