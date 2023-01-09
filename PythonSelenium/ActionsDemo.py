from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Users\\slaishet\\AppData\\Local\\Programs\\Python\\Python37-32\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

action = ActionChains(driver)
menu = driver.find_element_by_id("mousehover")

# the below action is executed only after giving perform method
action.move_to_element(menu).perform()

childMenu = driver.find_element_by_link_text("Top")
# Perform should be given to do the actions mandatorily
action.move_to_element(childMenu).click().perform()