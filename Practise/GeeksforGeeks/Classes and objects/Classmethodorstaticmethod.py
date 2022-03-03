class C(object):
    @classmethod
    def fun(cls,arg1,arg2):
        pass

"""A class method takes cls as the first parameter while a static method needs no specific parameters.
A class method can access or modify the class state while a static method can’t access or modify it.
In general, static methods know nothing about the class state. They are utility-type methods that take some parameters 
and work upon those parameters. On the other hand class methods must have class as a parameter.
We use @classmethod decorator in python to create a class method and we use @staticmethod decorator to create a static 
method in python.
"""

"""
When to use what?
We generally use class method to create factory methods. Factory methods return class objects 
( similar to a constructor ) for different use cases.
We generally use static methods to create utility functions.
"""

from datetime import  date

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls,name,year):
        return cls(name,date.today().year-year)

    @staticmethod
    def isAdult(age):
        return age > 18

person1 = Person('mayank',21)
person2 = Person.fromBirthYear('mayank22',1996)

print(person1.age)
print(person2.age)
print(person1.name)
print(person2.name)

print(Person.isAdult(22))
