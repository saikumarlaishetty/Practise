import time

from selenium import webdriver
from selenium.webdriver.support.select import Select

try :
    driver = webdriver.Chrome(executable_path="C:\\Users\\slaishet\\AppData\\Local\\Programs\\Python\\Python37-32\\chromedriver.exe")
    driver.get("https://rahulshettyacademy.com/angularpractice/")

    #driver.find_element_by_link_text("Shop").click()

    #driver.find_element_by_xpath()

    # driver.find_element_by_css_selector("input[name='name']").send_keys("SAIKUMAR")   # Find element by Name
    # #driver.find_element_by_xpath("//input[@name='email']").send_keys("l.saikumar5@gmail.com")     # find element by xpath
    # #driver.find_element_by_css_selector("input[id='exampleInputPassword1']").send_keys("saikumar")  #find element by css selector
    # # Generating css with ID
    # driver.find_element_by_css_selector("input#exampleInputPassword1").send_keys("SAIKUMAR")
    #
    # # generating css with class
    # driver.find_element_by_css_selector("input.ng-pristine").send_keys("l.saikumar5@gmail.im")
    #
    #
    # driver.find_element_by_class_name("btn-success").click()
    #
    # driver.find_element_by_id("exampleCheck1").click()
    # #print(driver.find_element_by_css_selector("[class*='alert-success']").text)
    # print(driver.find_element_by_xpath("//*[contains(@class,'alert-success')]").text)

    dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
    dropdown.select_by_index(1)
    time.sleep(5)
except Exception as e:
    print(e)
# finally:
#     driver.close()
