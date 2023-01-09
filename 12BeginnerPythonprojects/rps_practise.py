import random

def play():
    user_input = input(f'what is your choice ? r, p,s').lower()
    computer  = random.choice(['r','p','s'])
    if user_input == computer:
        return "TIE"
    elif is_win(user_input,computer):
        return "You Won"

    return "You False"

def is_win(player,opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p')\
        or(player == 'p' and opponent == 'r'):
        return True

print(play())


