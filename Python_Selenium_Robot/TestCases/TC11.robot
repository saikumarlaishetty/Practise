# Part 12- How to perform Mouse Operations in Robot Framework

*** Settings ***
Library     SeleniumLibrary


*** Test Cases ***
MouseActions
    # right click or open context menu
    open browser    http://swisnl.github.io/jQuer-contextMenu/demo.html     chrome
    maximize browser window

    # To right click on the webpage use "open context menu"
    open context menu  xpath://span[@class='context-menu-one btn btn-neutral']

    sleep   3
    close browser


    # double click action
    go to   https://testautomationpractice.blogspot.com/
    maximize browser window
    double click element  xpath://button[contains(text(),'Copy Text')]

    sleep   3


    # Drag and drop action
    go to  http://www.dhtml.goodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html
    maximize browser window
    # drag and drop <source> <target>
    drag and drop  id:box06    id:box106
    sleep   3

    close browser




