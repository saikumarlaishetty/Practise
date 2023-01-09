"""
We want to debug class methods, what we want
is that whenever the class method executes, it should print its
fully qualified name before executing its body.

The very first solution that comes to our mind is using method
decorators, following is the sample code –
"""

from functools import wraps

def debug(func):
    '''Decorators for debugging passed function'''

    @wraps(func)
    def wrapper(*args,**kwargs):
        print("Full name of this method :",func.__qualname__)
        return func(*args,**kwargs)
    return wrapper

def debugmethods(cls):
    '''Class decorator make use of debug decorator to debug class methods'''
    # check in class dictionary for any callable(method)
    # if exist, replace it with debugged version
    for key,val in vars(cls).items():
        if callable(val):
            setattr(cls,key,debug(val))
    return cls

# Sample class
#

@debugmethods
class Calc:
    def add(self, x, y):
        return x + y

    def mul(self, x, y):
        return x * y

    def div(self, x, y):
        return x / y


mycal = Calc()
print(mycal.add(2, 3))
print(mycal.mul(5, 2))
"""
The problem is if we have many such subclasses, then in that case
 we won’t like adding a decorator 
to each one separately. If we know beforehand that every subclass
 must have this debug property, then we should look up to the
  metaclass-based solution.
Have a look at this metaclass based solution, the idea is that 
classes will be created normally and then immediately 
wrapped up by debug method decorator – 
"""

from functools import wraps

def debug(func):
    '''decorators for debugging passed function'''

    @wraps(func)
    def wrapper(*args,**kwargs):
        print("Full name of this method :",func.__qualname__)
        return func(*args,**kwargs)
    return wrapper

def debugmethods(cls):
    '''class decorator make use of debug decorator'''
    for key,val in vars(cls).items():
        if callable(val):
            setattr(cls,key,debug(val))
    return cls

class debugMeta(type):
    """meta class which feed created class object to debugmethod
    to get debug functionality enabled objects"""
    def __new__(cls,clsname,bases,clsdict):
        obj = super().__new__(cls,clsname,bases,clsdict)
        obj = debugmethods(obj)
        return obj

# Base class with metaclass 'debugmeta' now all the subclass of this
# will have debugging applied

# inheriting Base
class Calc(Base):
    def add(self,x,y):
        return x+y

# inheriting Calc
class Calc_adv(Calc):
    def mul(self,x,y):
        return x*y

    # Now Calc_adv object showing debugging behaviour
mycal = Calc_adv()
print(mycal.mul(2,3))
