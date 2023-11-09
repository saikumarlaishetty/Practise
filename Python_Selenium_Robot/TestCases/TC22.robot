# Part 23- Page Object Model (POM) Pattern in Robot Framework | Selenium with Python

*** Settings ***
Library  SeleniumLibrary
Resource   ../Resources/loginKeywords.robot

*** Variables ***
${Browser}  chrome
${SiteUrl}  http://newtours.demoaut.com/
${user}     tutorial
${pwd}      tutorial


*** Test Cases ***
LoginTest
    open my Browser     ${SiteUrl}  ${Browser}
    Enter UserName  ${user}
    Enter Password  ${pwd}
    Click signIN
    Verify Successful Login
    close all browsers