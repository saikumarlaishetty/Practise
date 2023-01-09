#Python program to illustrate functions
def hello():
    print("hello")
    print("hello again")

hello()
# Calling function again
hello()

# python program to illustrate function with main
def getInteger():
    result = int(input("Enter integer: "))
    return result

def Main():
    print("Started")

    #Calling the getInteger function and store it in output variable
    output=getInteger()
    print(output)

#Now tell python about the main function existence
if __name__ == "__main__":
    Main()