# Part 13- User Defined Keywords & Resource Files in Robot Framework | Selenium with Python


# Normally keywords will be put in another file called resources to acheive reusability.

*** Settings ***
Library     SeleniumLibrary

*** Variables ***
${url}      http://www.newtours.demout.com/
${browser}  chrome

*** Keywords ***
lauchBrowserWithoutArguments
    open browser  ${url}     ${browser}
    maximize browser window

lauchBrowserWithArgs
    [Arguments]     ${appurl}   ${appbrowser}
    open browser  ${appurl}   ${appbrowser}
    maximize browser window

lauchBrowserWithArgsAndreturn
    [Arguments]     ${appurl}   ${appbrowser}
    open browser  ${appurl}   ${appbrowser}
    maximize browser window
    ${title}=   get title
    [Return]    ${title}






