# Part 17- How to Handle Web/HTML Table in Robot Framework | Selenium with Python

*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
TableValidations
    open browser  https://testautomationpractice.blogspot.com/  chrome
    maximize browser window
    # tr is table row
    ${rows}=    get element count  xpath://table[@name='BookTable']/tbody/tr
    # th is table header
    ${cols}=    get element count  xpath://table[@name='BookTable']/tbody/tr[1]/th

    log to console  ${rows}
    log to console  ${cols}

    # td is table data
    ${data}=    get text  xpath://table[@name='BookTable']/tbody/tr[5]/td[1]
    log to console  ${data}

    # table column should contain  <table location>   < column number >    <texttofind>
    table column should contain  xpath://table[@name='BookTable']   2   Author

    # table row should contain  <table location>   < row number >    <texttofind>
    table row should contain  xpath://table[@name='BookTable']   4      Learn JS

    # table cell should contain  <table location>   <row >  < column>    <texttofind>
    table cell should contain  xpath://table[@name='BookTable']   5  2   Mukesh

    # table header should contain  <table location>  <texttofind>
    table header should contain  xpath://table[@name='BookTable']   BookName

    close browser