

def digit_count(number, digit=9):
    temp = 0
    for num in range(int(number)):
        temp += int(str(num).count(digit))
    return temp


while True:
    number = input("Till what number would you like to count ?  or press q or Q to quit")
    if number.isdigit():
        digit = input("Which digit would you like to count ? or press q or Q to quit")
        if digit.isdigit():
            print("The number of ", digit," digits in ", number," is ",digit_count(number, digit))
        elif number == 'q' or 'Q':
            print("<---- Program aborted ---->")
            break
        else:
            print("Please enter only the digits between 0-9 ")
            print("press q or Q to quit")
    elif number == 'q'or 'Q':
        print("<---- Program aborted ---->")
        break
    else:
        print("Please enter only numbers")






