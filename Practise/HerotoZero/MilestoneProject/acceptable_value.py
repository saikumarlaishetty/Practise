"""
Edit the function to confirm against an acceptable value or type
"""

from os import system,name

def clear():
    if name == 'nt':
        _ = system('cls')

def user_choice():
    choice = 'wrong'

    while not choice.isdigit():
        choice = input("Please enter a number :")

        # Error Message Check
        if not choice.isdigit():
            clear()
            print("Sorry, but you did not enter an integer. Please try again.")

    return int(choice)


print(user_choice())


