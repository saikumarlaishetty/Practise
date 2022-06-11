import random

def guess(x):
    random_number = random.randint(1,x)
    guess_number = 0
    while guess_number != random_number:
        guess_number = int(input(f'Guess a number ?'))
        if guess_number > random_number:
            print("Too high")
        elif guess_number < random_number:
            print("Too low")

    return "Yay! you guessed right! "

#print(guess(10))


# computer guess

def computer(x):
    computer_number = random.randint(1,x)
    print(f'Computer number is {computer_number}')
    feedback = ''
    loop = 0
    user_number = int(input(f'Take a number'))
    print(f'User number is {user_number}')
    while feedback != 'C':
        print(f'Loop {loop} Computer number {computer_number}')
        print(f'Loop {loop} user number {user_number}')
        if computer_number > user_number:
            feedback = 'H'
            print(f'Feedback = {feedback}')
            computer_number = random.randint(1,computer_number-1)
        elif computer_number < user_number:
            feedback = 'L'
            print(f'Feedback = {feedback}')
            computer_number = random.randint(computer_number+1,x)
        else:
            feedback = 'C'
            print(f'Feedback = {feedback}')
            print(f'You have guessed it right in {loop} times')
            print(f' finally Computer number {computer_number}')
            print(f'finally user_number {user_number}')
            break
        loop = loop + 1

print(computer(10))
