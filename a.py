from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://www.udemy.com/")

webElement = driver.find_element(By.ID,"u201-popper-trigger--110").click()


time.sleep(50)
k dwnank
