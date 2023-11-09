# Part 22- Tags | Grouping Tests in Robot FrameworkRobot | Selenium with Python

*** Settings ***

*** Test Cases ***

TC1 User RegistrationTest
    [Tags]  regression
    log to console  This is user reg test
    log to console  user registration test is over

TC2 LoginTest
    [Tags]  sanity
    log to console  This is login test
    log to console  login test is over

TC3 change User settings
    [Tags]  regression
    log to console  This is changing user settings test
    log to console  change user settings test is over

TC4 LogoutTest
    [Tags]  sanity
    log to console  This is Logout test
    log to console  Logout test is over

# Noraml run : robot TC21.robot

# using tags
# run only sanity
# robot --include=sanity   TC21.robot
# robot -i sanity TC21.robot

# run only regression
# robot --include=regression   TC21.robot
# robot -i regression TC21.robot

# exclude sanity
# robot --execlude=sanity   TC21.robot
# robot -e sanity TC21.robot


# include sanity and execlude regression
# robot -i sanity -e regression TC21.robot