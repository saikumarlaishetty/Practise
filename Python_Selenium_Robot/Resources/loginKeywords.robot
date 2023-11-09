# Part 23- Page Object Model (POM) Pattern in Robot Framework | Selenium with Python

*** Settings ***
Library  SeleniumLibrary

# variables to import python files
Variables   ../PageObjects/Locators.py


*** Keywords ***
Open my Browser
    [Arguments]  ${SiteUrl} ${Browser}
    open browser  ${SiteUrl}    ${Browser}
    maximize browser window

Enter UserName
    [Arguments]  ${username}
    input text  {txt_loginUserName}  ${username}


Enter Password
    [Arguments]  ${password}
    input text  ${txt_loginPassword}    ${password}

Click signIN
    click button    ${btn_signIn}

Verify Successful Login
    title should be  Find a Flight:Mercury Tours:

close my browsers
    close all browsers



