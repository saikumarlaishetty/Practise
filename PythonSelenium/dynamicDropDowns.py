import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\slaishet\\AppData\\Local\\Programs\\Python\\Python37-32\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element_by_id("autosuggest").send_keys("Ind")
time.sleep(3)
countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
print("Countries = ", countries)
for country in countries:
    if country.text == "India":
        country.click()
        break
print("Ind", driver.find_element_by_id("autosuggest").text)
Attribute = driver.find_element_by_id("autosuggest").get_attribute('value')
print("Attribute ", Attribute)
assert Attribute == "India"





