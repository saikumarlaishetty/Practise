
def user():
    with open('users.txt', 'r') as file:
        users = file.readlines()
        users = [i.strip("\n") for i in users]
    while True:
        username = input("Enter your username : ").lower()
        if username not in users.lower():
            return True
            break
        print("Username already exists")

def password():
    while True:
        psw = input("Enter your password: ")
        notes =[]
        if not any(i.isdigit() for i in psw):
            notes.append("Password should contain atleast one number.")
        if not any(i.isupper() for i in psw):
            notes.append("Password should contain one upper case letter")
        if len(psw) < 5:
            notes.append("You need at least 5 characters")
        if len(notes) == 0:
            print("password is fine")
            break
        else:
            print("Please check the following")
            for note in notes:
                print(note)

if user():
    print("User is registered.")
password()
