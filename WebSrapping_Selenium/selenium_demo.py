#download Selenium driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chrome_driver_path = Service("C:\SeleniumDriver\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)

driver.get("https://www.amazon.com/Portable-Projector-Keystone-Correction-Battery/dp/B086R5YWW1/ref=psdc_300334_t3_B09MFS4M6H")
projector_price = driver.find_element(By.CLASS_NAME,"a-price-whole")

print(projector_price.text)
#driver.close() # This closes specific tab
driver.quit()    # This closes the entire tabs