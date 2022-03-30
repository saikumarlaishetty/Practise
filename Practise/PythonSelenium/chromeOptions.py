
from selenium import webdriver
from selenium.webdriver import ActionChains

chrome_options = webdriver.ChromeOptions()
# To start maximize chrome browser
chrome_options.add_argument("--start-maximized")

# To start headless browser
chrome_options.add_argument("headless")

# To ignore all the cert errors while opening the web page
chrome_options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(executable_path="C:\\Users\\slaishet\\AppData\\Local\\Programs\\Python\\Python37-32\\chromedriver.exe",options=chrome_options)

driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)