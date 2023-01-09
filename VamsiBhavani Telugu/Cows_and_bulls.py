from random import randint

def random():
    while True:
        n = str(randint(100,999))
        if not (n[0] == n[1] or n[1] == n[2] or n[2] == n[0]):
            return n



name = input("Welcome to the cows and bulls game \nPlease enter your name: ")
print("Hi",name)
chances = 5
cows = 0
bulls = 0

num = str(random())
while chances > 0 :
    print("You have ",chances,"chances left.")
    user = str(input("Enter your guess : "))
    if num == user:
        print("Great ! you got it right.")
        break
    else:
        for i in range(0,3):
            if user[i] == num[i]:
                bulls = bulls + 1
            elif user[i] in num:
                cows = cows + 1
        print("Keep going. You have",bulls,"bulls and",cows,"cows")
        bulls = 0
        cows = 0
        chances = chances - 1

print("The correct answer is ",num)
