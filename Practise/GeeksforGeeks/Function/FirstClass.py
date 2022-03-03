#  A programming language is said to support
#  first-class functions if it treats functions as first-class
#  objects.
#  Python supports the concept of First Class functions.

def shout(text):
    return text.upper()

print(shout('Hello'))

yell = shout
print(yell('Hello'))

# Functions can be passed as arguments to other functions

def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    greeting = func("""Hi, I'm created by a function
    passed as an argument""")
    print(greeting)

greet(shout)
greet(whisper)

# Functions can return another function
def create_adder(x):
    def adder(y):
        return x+y

    return adder

add_15 = create_adder(15)
print(add_15(10))