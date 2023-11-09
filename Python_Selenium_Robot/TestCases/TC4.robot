# Part5- How To Select Options from Drop-Down & List Boxes in Robot Framework | Selenium with Python

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

    # select options from drop down where single value is selected at atime.
    select from list by label   continents  Asia
    sleep   3
    select from list by index   continents  5


    # Select options from list boxes where we can select multiple values
    select from list by label   selenium_commands   Switch Commands
    select from list by label   selenium_commands   WebElement Commands
    sleep   3
    unselect from list by label
