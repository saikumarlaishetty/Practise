# Part 14- Scrolling Page using JavaScript executor in Robot Framework | Selenium with Python

*** Settings ***
Library     SeleniumLibrary

*** Test Cases ***
scrollingTest
    open browser  https://www.countries-of-the-world.com/flags-of-the-world.html    chrome
    maximize browser window

    # Scroll page till it reach a pixel number
    execute javascript  window.scrollTo(0,2500)

    # Scrolling page till find element on page
    scroll element into view  xpath://*[id="content"]/div[2]/img


    # scroll page till the bottom
    execute javascript  window.scrollTo(0,document.body.scrollHeight)   #end of the page

    sleep   5

    execute javascript  window.scrollTo(0,-document.body.scrollHeight)  #starting point



