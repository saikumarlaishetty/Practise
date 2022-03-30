from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\slaishet\\AppData\\Local\\Programs\\Python\\Python37-32\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_css_selector("#name").send_keys("Option3")
#driver.find_element_by_id("alertbtn").click()

# alert = driver.switch_to.alert
# print(alert.text)
# assert "Option3" in alert.text
# alert.accept()

driver.find_element_by_id("confirmbtn").click()
confirm = driver.switch_to.alert
print(confirm.text)
confirm.dismiss()
