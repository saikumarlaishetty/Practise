# Part 9- How to Handle Tabbed Windows & Browser Windows


*** Settings ***
Library     SeleniumLibrary


*** Test Cases ***
TabbedWindowsTest
    open browser  http://demo.automationtesting.in/windows.html     chrome
    click element  xpath://*[@id="Tabbed"]/a/button

    # After clicking on above element
    # there are two windows are present
    # We have to select a window using url or title
    # Here the title is been used
    select window   title=Sakinalium | Home

    # click on contact tab
    click element  xpath://*[@id="container"]/header/div/div/div[2]/ul/li[4]/a
    sleep   3
    close all browsers


mutlipleBrowsers
    open browser  https://www.google.com/   chrome
    maximize browser window

    sleep   3

    open browser  https://www.bing.com/     chrome
    maximize browser window

    # Browsers will have indexes starts with 1
    # Here google has index 1
    # and bing has index 2

    switch browser  1
    ${title}=   get title
    log to console  ${title}


    switch browser  2
    ${title}=   get title
    log to console  ${title}

    sleep   3
    close all browsers








