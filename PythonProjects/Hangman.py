name = input("What is your name ?")
print ("Good Morning " + name + " Lets play Hangman !!!")

word = "secret"
guesses = ""
turns = 10
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char,end=" ")
        else:
            print("_",end=" ")
            failed +=1
    if failed == 0:
        print("You won")
        break
    guess = input("Guess the character")
    guesses += guess
    if guess not in word:
        print("you are wrong")
        turns -=1
    if turns ==0:
        print("You loose")
        break
