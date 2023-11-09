
Part7- How to Close Single & Multiple Browsers in Robot Framework

*** Settings ***
# Libraries should be under this *** settings ***
Library  SeleniumLibrary

*** Test Cases ***
MyTestCase
    open browser  http://demowebshop.tricentis.com/register chrome
    maximize browser window

    open browser  http://automationpractice.com/index.php chrome
    maximize browser window

    # close the last opened browser
    close browser

    # closes all the browsers
    close all browsers


