# Part 19- Data Driven Testing Using Excel & CSV Files in Robot Framework | Selenium with Python

*** Settings ***
Library     SeleniumLibrary
Resource  C:/Users/slaishet/PycharmProjects/Practise/Python_Selenium_Robot/Resources/login_resources.robot
Library     DataDriver  C:/Users/slaishet/PycharmProjects/Practise/Python_Selenium_Robot/TestData/LoginData.csv

Suite Setup     Open my Browser
Suite Teardown  Close Browser
Test Template  Invalid login


*** Test Cases ***
LoginTcsWithCSV using ${username} and ${password}




*** Keywords ***
Invalid login
    [Arguments]  ${username} ${password}
    Input username  ${username}
    Input pwd   ${password}
    click login button
    Error message should be visible