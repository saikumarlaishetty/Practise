# Part 11- How to Capture Element & Full Page Screenshot | RobotFramework | Selenium with Python

*** Settings ***
Library     SeleniumLibrary


*** Test Cases ***
LoginTC
    open browser  https://opensource-demo.orangehrmlive.com     chrome
    input text  id:txtUsername  Admin
    input text  id:txtPassword  admin123

    # Path shouild have forward slash
    # This is used for caputre screen shot of element
    capture element screenshot  xpath://*[@id="divLogo"]/img    C:/Users/slaishet/PycharmProjects/Practise/Python_Selenium_Robot/TestCases/logo.png


    # To capture full page screenshot
    # This does not need any element like xpath,id or name
    # If you dont specify the location then it would be saved under the same folder by default.
    capture page screenshot  C:/Users/slaishet/PycharmProjects/Practise/Python_Selenium_Robot/TestCases/page.png