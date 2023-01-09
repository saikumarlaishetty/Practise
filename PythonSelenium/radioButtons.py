from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\slaishet\\AppData\\Local\\Programs\\Python\\Python37-32\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

radiobuttons = driver.find_elements_by_name("radioButton")
radiobuttons[2].click()            # Radio button 3 will be selected as list index starts from zero.
assert radiobuttons[2].is_selected()