# https://chercher.tech/practice/practice-pop-ups-selenium-webdriver

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Users\\slaishet\\AppData\\Local\\Programs\\Python\\Python37-32\\chromedriver.exe")

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")

action = ActionChains(driver)
action.context_click(driver.find_element_by_id("double-click")).perform()
action.double_click(driver.find_element_by_id("double-click")).perform()

clickOK= driver.switch_to.alert
clickOK.accept()
# To do a right click on a object use context

