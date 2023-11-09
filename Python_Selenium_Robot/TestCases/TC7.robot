# Part 8- How to Handle Alerts & Frames Robot Framework


*** Settings ***
Library     SeleniumLibrary


*** Test Cases ***
HandlingAlerts
    open browser    https://testautomationpractice.blogspot.com/    create chrome
    click element  xpath://*[@id="HTML9"]/div[1]/button     # open alert
    sleep   3

    #To handle the alert we have accept , dismiss and leave
    # accept is like pressing ok
    # dismiss is like pressing cancel
    # Leave is like leave the pop as is

    handle alert    accept
    handle alert    dismiss
    handle alert    leave

    # This is used to verify whether the alert contains the message "press a button"
    # It closes the alert windows after verification.
    alert should be present     Press a button!

    # a negative scenario
    alert should not be present    Press a button!


HandleFrames
    # You have to select a frame perform a action then unselect a frame then select other frame
    # and perform the aciton.
    open browser  https://seleniumhq.github.io/selenium/docs/api/java/index     chrome

    # We can use id, name or xpath in selecting a frame.
    # Frame 1
    select frame  packageListFrame
    click link  org.openqa.selenium
    unselect frame

    # Frame 2
    select frame  packageFrame
    click link   WebDriver
    unselect frame

    # Frame 3
    select frame  classFrame
    click link   Help
    unselect frame

    close browser