#Global variable
a = 15
b = 10


# Function to perform addition
def add():
    c = a + b
    print(c)


#Calling a function
add()


#non local keyword
def fun():
    var1 = 10

    def gun():
        # Tell python explicitly that it has to access var1
        # initilaized in fun on line 2
        # using the keyword nonlocal
        nonlocal var1

        var1 = var1 + 10
        print(var1)
    gun()
fun()
