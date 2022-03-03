# Meta class without type()
# Our metaclass


class MutliBases(type):
    # Overridding __new__ method
    def __new__(cls, clsname, bases, clsdict):
        # if no of base classes is greater than 1
        # raise error
        if len(bases) > 1:
            raise TypeError("Inherited multiple base classes!!!")

        # else execute __new__ method of super class i.e
        # call __init__ of type class
        return super().__new__(cls, clsname, bases, clsdict)


# Metaclass can be specified by 'metaclass' keyword argument
# now MultiBase class is use for creating classes
# this will be propagated to all the subclasses of Base
class Base(metaclass=MutliBases):
    pass

# no error is raised
class A(Base):
    pass

# no error is raised
class B(Base):
    pass

# This will raise an error!
class C(A,B):
    pass
