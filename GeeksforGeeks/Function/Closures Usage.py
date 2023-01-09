import logging
logging.basicConfig(filename = 'example.log',level= logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info('Running "{}" with arguments {}'.
                     format(func.__name__,args))

        print(func(*args))
    return log_func

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

add_logger = logger(add)
sub_logger = logger(sub)
add_logger(3,3)
sub_logger(4,5)

"""
When and why to use Closures:
1. As closures are used as callback functions, they provide some sort of data hiding. 
This helps us to reduce the use of global variables.

2.  When we have few functions in our code, closures prove to be an efficient way. 
But if we need to have many functions, then go for class (OOP)."""