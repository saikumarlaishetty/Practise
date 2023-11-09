# Part 18- Data Driven Testing Using Script in Robot Framework | Selenium with Python

*** Settings ***
Library     SeleniumLibrary
Resource  C:/Users/slaishet/PycharmProjects/Practise/Python_Selenium_Robot/Resources/login_resources.robot
Suite Setup     Open my Browser
Suite Teardown  Close Browser
Test Template  Invalid login


*** Variables ***
${LOGIN URL}    https://admin-demo.nopcommerce.com
${BROWSER}      chrome

*** Test Cases ***      username        password
Right user empty pass   admin@st.com    ${EMPTY}
Right user wrong pass   admin@st.com    xyz
Wrong user right pass   admin@st.com    admin
Wrong user empty pass   admin@st.com    ${EMPTY}
Wrong user wrong pass   admin@st.com    xyz



*** Keywords ***
Invalid login
    [Arguments]  ${username} ${password}
    Input username  ${username}
    Input pwd   ${password}
    click login button
    Error message should be visible