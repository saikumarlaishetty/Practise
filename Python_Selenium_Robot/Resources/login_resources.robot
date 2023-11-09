# Part 18- Data Driven Testing Using Script in Robot Framework | Selenium with Python

*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${LOGIN URL}    https://admin-demo.nopcommerce.com
${BROWSER}      chrome

*** Keywords ***
Open my Browser
    open browser  ${LOGIN URL}  ${BROWSER}
    maximize browser window

Close Browsers
    close all browsers

Open Login Page
    go to  ${LOGIN URL}


Input username
    [Arguments]   ${username}
    input text  id:Email    ${username}

Input pwd
    [Arguments]  ${password}
    input text  id:Password

click login button
    click element  xpath://input[@class='button-1 login-button']

click logout link
    click link  logout


Error message should be visible
    page should contain  Login was unsuccessful

Dashboard page shoudl be visible
    page should contain  Dashboard

