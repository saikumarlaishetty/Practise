# Part 15- How to work with FOR loop in Robot Framework | Selenium with Python

*** Test Cases ***
# For loop with numbers
forLoop1
    :   FOR {i}     IN RANGE    1  10
    \   log to console  ${i}

# For loop with numbers
forLoop2
    # with one space between 1 2 3 4 5 it prints on the same line
    # with two spaces between 1  2  3  4  5 prints on the different line
    :   FOR {i}     IN RANGE    1 2 3 4 5
    \   log to console  ${i}

forLoop3withlist
    # with one space between 1 2 3 4 5 it prints on the same line
    # with two spaces between 1  2  3  4  5 prints on the different line
    @{items}    create list     1 2 3 4 5
    :   FOR {i}     IN RANGE    @{items}
    \   log to console  ${i}

forLoop4
    # with one space between john david smith scott it prints on the same line
    # with two spaces between john  david  smith  scott prints on the different line
    :   FOR {i}     IN RANGE    john david  smith   scott
    \   log to console  ${i}

forLoop5
    # with one space between john david smith scott it prints on the same line
    # with two spaces between john  david  smith  scott prints on the different line
     @{namelist}    create list     john david  smith   scott
    :   FOR {i}     IN RANGE    @{namelist}
    \   log to console  ${i}

forloop6withExit
    # with one space between 1 2 3 4 5 it prints on the same line
    # with two spaces between 1  2  3  4  5 prints on the different line
    :   FOR {i}     IN RANGE    1 2 3 4 5
    \   log to console  ${i}
    \   exit for loop if  {i}==3




