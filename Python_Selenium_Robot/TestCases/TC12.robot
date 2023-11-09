# Part 13- User Defined Keywords & Resource Files in Robot Framework | Selenium with Python


# Normally keywords will be put in another file called resources to acheive reusability.

*** Settings ***
Library     SeleniumLibrary
Resource    C:/Users/slaishet/PycharmProjects/Practise/Python_Selenium_Robot/Resources/resources.robot

*** Variables ***
${url}      http://www.newtours.demout.com/
${browser}  chrome


*** Test Cases ***
TC1
    lauchBrowserWithoutArguments
    input text  name:userName   mercury
    input text  name:password   mercury

TC2
    lauchBrowserWithArgs  ${url}    ${browser}
    input text  name:userName   mercury
    input text  name:password   mercury

TC3
    ${pageTitle}=   lauchBrowserWithArgsAndreturn   ${url}    ${browser}
    log to console      ${pageTitle}

    # This will help to print the output in the report
    log     ${pageTitle}

    input text  name:userName   mercury
    input text  name:password   mercury







