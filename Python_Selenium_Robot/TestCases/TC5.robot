# Waits & TimeOuts in Robot Framework | Selenium Speed

*** Settings ***
# Libraries should be under this *** settings ***
Library  SeleniumLibrary

*** Test Cases ***
seleniumspeed

    # Get default selenium get selenium speed
    ${speed}=   get selenium speed
    log to console      ${speed}
    # Here speed by default 0

    open browser  http://demowebshop.tricents.com/register      chrome
    maximize browser window

    # every statement executes with 3 seconds delay
    set selenium speed  3 seconds

    select radio button     Gender      M
    input text  name:FristName      David
    input text  name:LastName       John
    input text  name:Email          anhc@gmail.com
    input text  name:Password       davidJohn
    input text  name:ConfirmPassword    davidJohn


    ${speed}=   get selenium speed
    log to console      ${speed}
    # here the selenium speed will be 3

    close browser


SeleniumTimeout

    # get the default selenium timeout
    ${time}=    get selenium timeout
    log to console  ${time}

    open browser  http://demowebshop.tricents.com/register      chrome
    maximize browser window

    # set the default selenium timeout
    set selenium timeout   10 seconds

    # set selenium timeout is applicable only for the wait until page not entirely.
    # Selenium waits until the page contains the register.
    # What is the default timeout ? Its 5 seconds
    wait until page contains    Register

    select radio button     Gender      M
    input text  name:FristName      David
    input text  name:LastName       John
    input text  name:Email          anhc@gmail.com
    input text  name:Password       davidJohn
    input text  name:ConfirmPassword    davidJohn

    close browser


ImplicitWait
    # Implict wait is more efficient

    ${implicttime}=     get selenium implicit wait
    log to console  ${implicttime}

    open browser  http://demowebshop.tricents.com/register      chrome
    maximize browser window

    # set selenium implicit wait
    # This will wait max 10 seconds for a locator if it finds in 1 second it goes to next step.
    # Implict wait is applicable to all the statements.
    set selenium implicit wait  10 seconds

    select radio button     Gender      M
    input text  name:FristName      David
    input text  name:LastName       John
    input text  name:Email          anhc@gmail.com
    input text  name:Password       davidJohn
    input text  name:ConfirmPassword    davidJohn

    ${implicttime}=     get selenium implicit wait
    log to console  ${implicttime}

    close browser