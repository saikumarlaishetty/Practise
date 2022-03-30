# Validate Whether products selected in Page 1 are showing in Page 2 check page.


# implicit wait - will be applied for all over the program


import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

list = []
itemlist = []
driver = webdriver.Chrome(executable_path="C:\\Users\\slaishet\\AppData\\Local\\Programs\\Python\\Python37-32\\chromedriver.exe")
# wait until 5 seconds if object is not displayed
driver.get("https://rahulshettyacademy.com/seleniumPractise/")

driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")

time.sleep(2)

count = driver.find_elements_by_xpath("//div[@class='products']/div")
assert len(count) == 3

buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")

# To get the vegetable name from the xpath and not using more for loops
for button in buttons:
    # this is how you go from child to parent tag and get the value
    list.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    button.click()

print(list)

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

items = driver.find_elements_by_css_selector("p.product-name")

for item in items:
    itemlist.append(item.text)

veggies = []
for i in itemlist:
    if i.strip() != '':
        veggies.append(i)

print(veggies)

assert veggies == list

wait = WebDriverWait(driver,5)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_class_name("promoBtn").click()

wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"span.promoInfo")))
print(driver.find_element_by_css_selector("span.promoInfo").text)

