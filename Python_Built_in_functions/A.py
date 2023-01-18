# abs - To return the absolute value of a number

print(abs(9))    # evaluates to 9
print(abs(9*5))  # evaluates to 45
print(abs(-9.0))  # evaluates to 9.0


# all(iterable) - Return true if all the elements of the iterable are true

"""
Learning: Use this kind of functions while writing your programs when you want to evaluate a condition like - (any(iterable))
            all the elements to be True

def all(iterable):
    for element in iterable:
        if not element:
            return False
    return True 

"""
iterable_1 = [1,0,0]
iterable_2 = [True, True, False]
iterable_3 = [True,True, True]

print("all -",(all(iterable_1)))
print("all -",(all(iterable_2)))
print("all -",(all(iterable_3)))

# any(iterable) - Return true if any of the iterable is True

"""
Learning : Use this kind of functions while writing your progams when you want to evaluate a condition like - all(iterbale)
            any elements to be true

def any(iterbale):
    for element in iterable:
        if element:
            return True
    return False

"""

iterable_1 = [1,0,0]
iterable_2 = [True, True, False]
iterable_3 = [False,False, False]

print("any - ",(any(iterable_1)))
print("any - ",(any(iterable_2)))
print("any - ",(any(iterable_3)))


# Ascii - Returns a readable version of an object. Replaces non-ascii characters with escape characters

x = ascii("My name is Ståle")
print("ascii - ", x)

# Bin - The bin function returns the binary version of a specified integer
b = bin(36)
print("bin - ",b)

# Bool(x) - Returns a boolean Value.

print(bool(1))
print(bool(None))
print(bool(0))
print(bool([]))
print(bool(False))


# bytearray - function returns a bytearray object
print(bytearray(1))

# bytes - Returns a byte object
print(bytes(1))

# callable - Returns true if the specified object is callable, otherwise False
def x():
    return 5

print(callable(x))

# chr - Returns the character that represent the specified unicode
print("Chr() - ",chr(97))
print("chr() - ",chr(98))

# Classmethod - Converts a method into a class method.
"""
A classmethod receives the class as implicit first argument, just like an instance method receives the instance.
class C:
    @classmethod
    def f(cls,arg1,agr2..):
    ....
     
"""

# Compile - Returns the specified source as a code object, ready to be executed.
x = compile('print(55)', 'test', 'eval')
exec(x)

# Complex - Returns a complex number by specifying a real number and an imaginary number
print(complex('3+5j'))
print(complex(3,5))

# Delattr- Delete the specified attribute from the specified object.

class Person:
    name = "John"
    age = 36

print(delattr(Person,'name'))


# Dict - This function creates a dictionary
x = dict(name = "John", age = 36, country = "Norway")
print(x)

# dir - The dir function returns all the properties and methods of a specified object, without the values.
print(dir(Person))

# divmod() - returns a tuple containing the quotient and the remainder when arg1 (dividend) is divided by arg2 ( divisor)
x = divmod(5,2)
print(x)

# enumerate - The enumerate function takes a collection(eg: tuple) and returns an enumerate object.
#           - The enumerate function adds a counter as the key of the enumerate object.
x = ('apple','banana','cherry')
y = enumerate(x)
print(list(y))

print(list(enumerate(x,start=1)))

"""
Learning : Usage of Yield statement saves memory.

def enumerate(iterable,start=0)
    n = start
    for elem in iterable:
        yield n,elem
        n+1
        
"""

# eval - Evaluates and executes an expression.
x = 'print(55)'
eval(x)

# exec - The exec function executes the specified python code.
# exec - This accepts large blocks of code, unlike the eval() function which only accepts a single expression.
x = 'name = "John"\nprint(name)'
exec(x)

# filter - Use a filter function to exclude items in an iterable object.
# filter(function,iterable)

ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True


adults = filter(myFunc, ages)
print(list(adults))

# float - converts the specified value into a floating point number
print(float(3))


# format - formats a specified value into a specified format
# format(value,format)
print(format(0.5,'%'))

# frozenset - returns an unchangeable forzenset object.
mylist = ['apple', 'banana', 'cherry']
x = frozenset(mylist)
print(x)

# getattr() - Returns the value of a specified attribute from the specified object.
x = getattr(Person,'age')
print(x)
y = getattr(Person,'doesnotexist','default message if attribute does not exist')
print(y)

# globals() function returns the global symbol table as a dictionary
x = globals()
print(x)
print(x['__file__'])

# hasattr - returns True if the specified object has specified attribute, otherwise False.
print(hasattr(Person,'age'))
print(hasattr(Person,'doesnotexist'))

# hash - returns hash value of a specified object.

# help - Executes the built in help system.

# hex - Converts a  number into a hexadecimal value
print(hex(123))

# id () - returns unique id for an object.
x = ('apple', 'banana', 'cherry')
y = id(x)
print(y)

# input() - Allows user input

# int() - returns an integer number

# isinstance() - Returns true if a specified object is an instance of an specified object.
print(isinstance(5,int))

# issubclass() - Returns True if a specified class is a subclass of a specified object
class myAge:
  age = 36

class myObj(myAge):
  name = "John"
  age = myAge

x = issubclass(myObj, myAge)
print(x)

# iter () - Returns an iter object
# next() - The next() function returns the next item in an iterator.
x = iter(["apple", "banana", "cherry"])
print(next(x))
print(next(x))
print(next(x))

# len() - returns length of an object
print(len('saikumar'))

# list - returns a list
x = list(('apple', 'banana', 'cherry'))
print(x)

# locals - returns local symbol table as dictionary
x = locals()
print(x)

# map - function executes a specified function for each item in an iterable.

""" Difference between map and filter ?????????????????????????????????????????????"""

def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))
print(list(x))


# max - returns the highest value , or the item with the highest value in iterable
print(max(1,2,3,4))

# memoryview - returns a memory view object from a specified object.
x = memoryview(b"Hello")

print(x)

#return the Unicode of the first character
print(x[0])

#return the Unicode of the second character
print(x[1])


# min () - returns the smallest item in an iterable.
print(min(5,10))

# object() - returns an empty object.

""" Use of an object function  ???????????????????????????????????????????????????"""

print(object())

# oct()- converts a number into an octal.
print(oct(12))

# open() - open a file and return a file object

# ord() -  	Convert an integer representing the Unicode of the specified character
x = ord("h")
print(x)

# pow () - returns the value of x to the power of y
print(pow(2,3))

# print()- prints to the standard output device

# property () - Gets, sets, deletes a property

# range () - Returns a sequence of numbers, starting from 0 and increments by 1(default)
# range(start,stop,step)
for i in range(1,10,3):
    print(i)

# repr() - Returns a readable version of an object

""" Execute the repr ?????????????????????????????????????????????????????"""

print(repr(Person))
print(Person)

# reversed() - Returns a reversed iterator
alph = ["a", "b", "c", "d"]
ralph = reversed(alph)
for x in ralph:
  print(x)

# round() - rounds a number
x = round(5.76543, 2)
print(x)

# set() - returns a new set object
x = set(('apple', 'banana', 'cherry','banana'))
print(x)

# setattr() - Sets an attribute(property/method) of an object
class Person:
  name = "John"
  age = 36
  country = "Norway"

setattr(Person, 'age', 40)

print(Person.age)

# slice() - Returns a slice object
a = ("a", "b", "c", "d", "e", "f", "g", "h")
x = slice(2)
print(a[x])

# sorted() - Returns a sorted list
a = ("b", "g", "a", "d", "f", "c", "h", "e")
x = sorted(a)
print(x)
print(a)

# str()- returns a str object

# sum() - sums the items of an iterator


# super() - The super() function is used to give access to methods and properties of a parent or sibling class.
# The super() function returns an object that represents the parent class.
class Parent:
  def __init__(self, txt):
    self.message = txt

  def printmessage(self):
    print(self.message)

class Child(Parent):
  def __init__(self, txt):
    super().__init__(txt)

x = Child("Hello, and welcome!")

x.printmessage()

# tuple()  - returns a tuple

# type() - returns type of an object

# vars() - returns a dict property of an object
class Person:
  name = "John"
  age = 36
  country = "norway"

x = vars(Person)
print(x)

# zip () - The zip() function returns a zip object, which is an iterator of tuples where the first item in each passed
#          iterator is paired together, and then the second item in each passed iterator are paired together etc.

a = ("John", "Charles", "Mike")
b = ("Jenny", "Christy", "Monica")

x = zip(a, b)
print(dict(x))