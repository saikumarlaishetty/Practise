import random
user_wins = 0
computer_wins = 0

options = ["rock", "papers", "scissors"]

while True:
    user_input = input("Type rock/papers/scissors or Q to quit :").lower()
    if user_input == "q":
        break

    if user_input not in ["rock", "papers", "scissors"]:
        continue

    random_number = random.randint(0, 2)
    # rock : 0 , paper : 1, Scissors : 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == 'rock' and computer_pick == "scissors":
        print("You won")
        user_wins += 1

    elif user_input == 'papers' and computer_pick == "rock":
        print("You won")
        user_wins += 1

    elif user_input == 'scissors' and computer_pick == "paper":
        print("You won")
        user_wins += 1

    elif user_input == computer_pick:
        print("Draw")

    else:
        print("You Lost")
        computer_wins += 1

print("Your score "+ str(user_wins))
print("Computer score ", computer_wins)
print("GoodBye")
