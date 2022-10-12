from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# 
# articles = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")
# 
# # print(articles.click())
# 
# all_portals = driver.find_element(by=By.LINK_TEXT, value="Current events")
# # all_portals.click()
# 
# search = driver.find_element(by=By.NAME, value="search")
# search.send_keys("Royal Enfield Himalayan")
# search.send_keys(Keys.ENTER)

driver.get("http://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(by=By.NAME, value="fName")
fname.send_keys("Prem")

lname = driver.find_element(by=By.NAME, value="lName")
lname.send_keys("S")

email = driver.find_element(by=By.NAME, value="email")
email.send_keys("prem@gmail.com")

btn = driver.find_element(by=By.CLASS_NAME, value="btn")
btn.send_keys(Keys.ENTER)

# driver.quit()