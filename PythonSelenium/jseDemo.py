# JS DOM can access any elements on web page just like how seleniume does
# selenium have a method to execute javascript code in it

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="C:\\Users\\slaishet\\AppData\\Local\\Programs\\Python\\Python37-32\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_name("name").send_keys("hello")
print(driver.find_element_by_name("name").text)  # empty output

#print(driver.find_element_by_name("name").get_attribute("value"))  #

# selenium is giving control to the java script
# this is purley java script if you feel selenium is not picking correctly then use java script like below
print(driver.execute_script('return document.getElementsByName("name")[0].value')) # goto console enter document. we see all the java script methods

# Through java script we can get the value like above and we can click on any webelement like below
# if selenium is unable to click a value then use java script like below
# A semicolon in java script is treated as complete step like "arguments[0].click();"
shopButton = driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script("arguments[0].click();",shopButton)

# Selenium does not scroll down the we need to use java script to do it
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")