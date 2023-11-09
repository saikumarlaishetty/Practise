# Part 16- How to Count & Extract Link Texts in Robot Framework | Selenium with Python


*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
GetAllLinksTest
    open browser  http://www.newtours.demout.com/   chrome
    maximize browser window
    ${Alllinkscount}=   get element count  xpath://a
    log to console  ${Alllinkscount}

    # To get the text of the links
    : FOR   ${i}    IN RANGE    1   ${Alllinkscount}+1
    # syntax to get text is <id/xpath/name>:(<//a>)[<number>]
    \   ${linkText}=    get text    xpath:(//a)[${i}]
    \   log to console  ${linkText}

