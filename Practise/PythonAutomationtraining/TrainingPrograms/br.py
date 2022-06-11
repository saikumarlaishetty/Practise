from selenium import webdriver
# Edge & Webdriver full path
dpath = "C:\\Users\\slaishet\\Desktop\\Office\\Automation\\edgedriver_win64\\msedgedriver.exe"
driver = webdriver.Edge(dpath)
url = "https://weather.com"
driver.get(url)
#driver.implicitly_wait(10)
#print(driver)
#driver.close()