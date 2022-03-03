def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def greet(func):
    greeting = func("Hi,I am created by a fun as a argument")
    print(greeting)


greet(shout)
greet(whisper)

