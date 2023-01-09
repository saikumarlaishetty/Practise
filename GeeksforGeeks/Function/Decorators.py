# Decorator can modify the behaviour
def h(func):
    def inner1():
        print("Hello, this is before function execution")
        func()
        print("This is after function execution")
    return inner1

def f_to_use():
    print("This is inside the function  !!!!")

f_to_use = h(f_to_use)

f_to_use()

# Execution time of a function
import time
import math

def calculate_time(func):
    def inner1(*args,**kwargs):
        begin = time.time()
        func(*args,**kwargs)
        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)
    return inner1

@calculate_time
def factorial(num):
    time.sleep(2)
    print(math.factorial(num))


factorial(10)

