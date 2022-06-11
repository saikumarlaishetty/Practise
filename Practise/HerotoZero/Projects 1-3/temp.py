import random

num = random.randint(1,100)

print("Lets Play")

guesses = [0]

while True:
    guess = int(input("What is your guess ?"))
    if guess < 1 or guess > 100:
        print("Out of bounds !")
        continue

    if guess == num:
        print("No of guesses ",len(guesses))
        break

    guesses.append(guess)
    if guess[-2]:
        if abs(num-guess) < abs(num-guesses[-2]):
            print('WARMER !')
        else:
            print('COLDER!')
    else:
        if abs(num-guess) <=10:
            print('WARM')
        else:
            print('COLD')
