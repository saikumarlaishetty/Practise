# Part10-Browser related Keywords | Robot Framework | Go To | Go Back | Get Location

*** Settings ***
Library     SeleniumLibrary


*** Test Cases ***
NavigationTest
    open browser  https://www.google.com     chrome
    # Get location gets the current opened URL
    ${loc}=     get location
    log to console  ${loc}

    # go to used to go to the url specified on the same tab
    go to  https://www.bing.com
    ${loc}=     get location
    log to console  ${loc}

    # go back used to go back to previous url
    # here it is google.com
    go back
    ${loc}=     get location
    log to console  ${loc}

    sleep   3
    close browser



