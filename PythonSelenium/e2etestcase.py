from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PythonSelenium.ExplicitWait import wait

driver = webdriver.Chrome(executable_path="C:\\Users\\slaishet\\AppData\\Local\\Programs\\Python\\Python37-32\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_css_selector("a[href*='shop']").click()

products = driver.find_elements_by_xpath("//div[@class='card h-100']")
for product in products:
    productName = product.find_element_by_xpath("div/h4/a").text
    if productName == 'Blackberry':
        #Add item to cart
        product.find_element_by_xpath("div/button").click()
        break

driver.find_element_by_css_selector("a[class*='btn-primary']").click()
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()

driver.find_element_by_css_selector("#country").send_keys("Ind")

wait = WebDriverWait(driver,7)
wait.until(expected_conditions.presence_of_element_located(By.LINK_TEXT,"India"))
driver.find_element_by_link_text("India").click()

driver.find_elements_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_css_selector("[type='submit']").click()

assert (driver.find_elements_by_css_selector("[class*='alert-success']").text) == "Success! Thank you! Your order will be delivered in next few weeks :-)"

# To get screenshot in selenium use below method
driver.get_screenshot_as_file("screen.png")

