from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
# price = driver.find_element(by=By.CLASS_NAME, value="a-price-whole")

# price = driver.find_element(by=By.CLASS_NAME, value="a-price-whole")
# print(price.text)

# search_bar = driver.find_element(by=By.NAME, value="q")
# print(search_bar.tag_name)

# event = driver.find_element(by=By.TAG_NAME, value="ul")
event_time = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget time")
event_name = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget ul a")

for e in event_time:
    print(e.text)

for a in event_name:
    print(a.text)


driver.quit()
