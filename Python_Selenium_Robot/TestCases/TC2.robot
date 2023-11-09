# How To Handle Input Box in Robot Framework

*** Settings ***
# Libraries should be under this *** settings ***
Library  SeleniumLibrary

*** Variables ***
${broswer}  chrome
${url}  https://demo.nopcommerce.com/


*** Test Cases ***
TestingInputBox
    open browser    ${url}    ${broswer}
    maximize browser window
    title should be     nopCommerce demo store
    click link  xpath://a[@class='ico-login']
    ${"email_txt"}  set variable  id:Email

    element should be visible  ${"email_txt"}
    element should be enabled   ${"email_txt"}

    input text   ${"email_txt"}   JohnDavid@gmail.com
    sleep   5
    clear element text
    sleep   3
    close browser
