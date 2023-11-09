# First test case in robotframework


*** Settings ***
# Libraries should be under this *** settings ***
Library  SeleniumLibrary

*** Variables ***
${broswer}  chrome
${url}  https://demo.nopcommerce.com/




*** Test Cases ***
# Name of the test case is login
LoginTest
    #create webdriver    chrome  executable_path="C:\Users\slaishet\Downloads\chromedriver_win32\chromedriver.exe"
    open browser    ${url}  ${broswer}
    loginToApplication
    close browser



*** Keywords ***
loginToApplication
    click link  xpath:/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a
    input text  id:Email  pavanoltraining@gmail.com
    input text  id:Password Test@123
    click element  xpath://input[@class='button-1 login-button']