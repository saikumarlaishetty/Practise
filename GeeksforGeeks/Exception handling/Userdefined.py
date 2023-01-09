class MyError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


try:
    raise(MyError(3*2))
except MyError as error:
    print("A new exception occured : ",error.value)



# Deriving  error from super class Exception
class Error(Exception):
    pass

class TransitionError(Error):
    def __init__(self,prev,nex,msg):
        self.prev = prev
        self.next = nex
        self.msg = msg

try:
    raise(TransitionError(2,3*2,"Not Allowed"))
except TransitionError as error:
    print("Exception occured :", error.msg)


# How to use standard exception as a base class
class Networkerror(RuntimeError):
    def __init__(self,arg):
        self.args = arg

try:
    raise Networkerror("Error")
except Networkerror as e:
    print(e.args)

