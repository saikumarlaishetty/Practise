#Method #1: Naive Method (Without using Regex).

#Password validation in Python
# using naive method

# Function to validate the password
def password_check(passwd):

    SpecialSym =['$', '@', '#', '%']
    val = True

    if len(passwd) < 6:
        print('length should be at least 6')
        val = False

    if len(passwd) > 20:
        print('length should be not be greater than 8')
        val = False

    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False

    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False

    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False

    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@#')
        val = False
    if val:
        return val

# Main method
def main():
    passwd = 'Geek12@'

    if (password_check(passwd)):
        print("Password is valid")
    else:
        print("Invalid Password !!")

# Method 2 with regex
import re


def main():
    passwd = 'Geek12@'
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"

    # compiling regex
    pat = re.compile(reg)

    # searching regex
    mat = re.search(pat, passwd)

    # validating conditions
    if mat:
        print("Password is valid.")
    else:
        print("Password invalid !!")


# Driver Code
if __name__ == '__main__':
    main()


# Driver Code
if __name__ == '__main__':
    main()