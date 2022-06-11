while False:
    psw = input("Enter new password: ")
    if any(i.isdigit() for i in psw):
        if any(i.isupper() for i in psw):
            if len(psw) >= 5:
                print("Password is fine")
                break
            print("Password need atleast 5 character")
        print("Need atleast one upper case")
    print("Password need atleast one digit")

#or

while True:
    notes = []
    psw = input("Enter password: ")
    if not any(i.isdigit() for i in psw):
        notes.append("You need at least one number")
    if not any(i.isupper() for i in psw):
        notes.append("You need at least one uppercase letter")
    if len(psw) < 5:
        notes.append("You need at least 5 characters")
    if len(notes) == 0:
        print("Password is fine")
        break
    else:
        print("Please check the following: ")
        for note in notes:
            print(note)