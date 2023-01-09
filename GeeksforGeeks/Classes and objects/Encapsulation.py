#  To prevent accidental change, an object’s variable
#  can only be changed by an object’s method.
#  Those types of variables are known as private variable.

# To accomplish this in Python, just follow the convention by
# prefixing the name of the member by a single underscore “_”.

#Base class
class Base:
    def __init__(self):
        # Protected member
        self._a = 2


# Derived class
class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling protected member of base class")
        self._a = 6
        print(self._a)


obj1 = Derived()
obj2 = Base()


# Calling protected member outside class will result in Attribute error
#print(obj2._a)


