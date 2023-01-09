"""
This whole meta thing can be summarized
as – Metaclass create Classes and Classes creates objects

__new__(): It’s a method which is called before __init__().
 It creates the object and returns it. We can override this method
 to control how the objects are created.
__init__(): This method just initialize the created object
 passed as a parameter

"""


def test_method(self):
    print("This is the test method! ")

# Creating a base class
class Base:
    def myfun(self):
        print("This is inherited method!")


# Creating Test class dynamically using type() method directly
Test = type('Test',(Base,),dict(x="atul",my_method= test_method))

# print type of Test
print("Type of Test class: ", type(Test))

# Creating instance of Test class
test_obj = Test()
print("Type of test_obj :",type(test_obj))

# Calling inherited method
test_obj.myfun()

# Calling Test class method
test_obj.my_method()

# Printing variable
print(test_obj.x)






