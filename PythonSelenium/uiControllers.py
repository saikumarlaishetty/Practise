from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\slaishet\\AppData\\Local\\Programs\\Python\\Python37-32\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# To click check boxes
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()




