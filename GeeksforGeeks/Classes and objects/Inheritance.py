# python code to demonstrate how parent constructors are called
class Person(object):
    # __init__ is known as the constructor
    def __init__(self,name,number):
        self.name = name
        self.number = number
    def display(self):
        print(self.name)
        print(self.number)

#Child class
class Employee(Person):
    def __init__(self,name,number,salary,post):
        self.salary = salary
        self.post = post
        # invoking the __init__ of the parent class
        Person.__init__(self,name,number)

a = Employee('Rahul',99,2000000,"Intern")
a.display()