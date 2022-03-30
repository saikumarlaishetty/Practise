from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Users\\slaishet\\AppData\\Local\\Programs\\Python\\Python37-32\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

print(driver.find_element_by_id("displayed-text").is_displayed())  # returns True

driver.find_element_by_id("hide-textbox").click()

print(driver.find_element_by_id("displayed-text").is_displayed())  # returns False

assert not (driver.find_element_by_id("displayed-text").is_displayed())