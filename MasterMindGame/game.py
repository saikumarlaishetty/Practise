import random

COLORS = ["R","G","Y","O","W","B"]
CODE_LENGTH = 4
TRIES = 10

def generate_code():
    """
    This function will return the guess code by the user
    :return: code :
    """
    code = []

    # Generates random color code
    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)

    return code


def guess_code():
    """
    Function to guess correct code.
    :return: Guess:"List"
    """

    while True:
        guess = input("Guess:").upper().split(" ")

        if len(guess) != CODE_LENGTH:
            print(f"you must guess {CODE_LENGTH} colors")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"Invalid color {color}. Try again")
                break
        else:
            break

    return guess

def check_code(guess,real_code):

    color_counts = {}
    incorrect_position = 0
    correct_position = 0

    # To get the number of colors and color counts
    for color in real_code:
        if color not in color_counts:
            color_counts[color] =0
        color_counts[color] += 1

    # To calculate the correct_position
    for guess_color,real_color in zip(guess,real_code):
        if guess_color == real_color:
            correct_position += 1
            color_counts[guess_color] -= 1

    # TO calculate the incorrect position
    for guess_color,real_color in zip(guess,real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_position += 1
            color_counts[guess_color] -= 1

    return correct_position,incorrect_position

def game():
    """
    Main function to run the game
    :return:
    """
    print(f"Welcome to Master mind , you have {TRIES} to guess the code")
    print(f"The valid colors are ",*COLORS)

    code = generate_code()

    for attempts in range(1,TRIES + 1):
        guess = guess_code()
        correct_pos,incorrect_pos = check_code(guess,code)

        if correct_pos == CODE_LENGTH:
            print(f"You guessed the code in {attempts} tries")
            break

        print(f"Correct positions : {correct_pos} | Incorrect Positions : {incorrect_pos}")

    else:
        print("You ran out of tries , the code was ",*code)


if __name__ == '__main__':
    # Code to test generate code
    # code = generate_code()
    # print(code)

    game()