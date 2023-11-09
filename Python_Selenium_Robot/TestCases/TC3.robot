
# How To Select Radio Buttons & Check Boxes in Robot Framework

*** Settings ***
# Libraries should be under this *** settings ***
Library  SeleniumLibrary

*** Variables ***
${broswer}  chrome
${url}  http://www.practiceselenium.com/practice-form.html


*** Test Cases ***
Testing Radio Buttons and Check Boxes
    open browser    ${url}    ${broswer}
    maximize browser window

    # Selecting Radio button
    select radio button  sex    Female
    select radio button  sex    5

    # selecting check box
    select checkbox  BlackTea
    select checkbox  RedTea

    unselect checkbox  BlackTea



