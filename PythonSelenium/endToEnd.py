# implicit wait - will be applied for all over the program


import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\slaishet\\AppData\\Local\\Programs\\Python\\Python37-32\\chromedriver.exe")
# wait until 5 seconds if object is not displayed
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/")

driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")

time.sleep(2)

count = driver.find_elements_by_xpath("//div[@class='products']/div")
assert len(count) == 3

buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    button.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()
#driver.find_element_by_xpath("//div[@class='action-block']/button").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
#driver.find_element_by_xpath("//div[@class='promoWrapper']/input").send_keys("rahulshettyacademy")
driver.find_element_by_class_name("promoBtn").click()