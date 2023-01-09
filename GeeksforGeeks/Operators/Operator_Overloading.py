# Python program to illustrate how to
# overload an binary + operator


class A:
    def __init__(self,a):
        self.a = a

    # adding two objects
    def __add__(self, other):
        return self.a + other.a


ob1 = A(1)
ob2 = A(2)
ob3 = A("Geeks")
ob4 = A("For")

print(ob1 + ob2)
print(ob3 + ob4)


# Adding two complex numbers
class complex:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return  self.a+other.a , self.b+other.b


ob1 = complex(1,2)
ob2 = complex(3,4)
ob3 = ob1 + ob2
print(ob3)


# Python program to overload a comparision operators
class A:
    def __init__(self,a):
        self.a = a
    def __gt__(self, other):
        if (self.a>other.a):
            return True
        else:
            return False

ob1 = A(2)
ob2 = A(3)
if ob1 > ob2:
    print("ob1 is greater than ob2")
else:
    print("ob2 is greater than ob1")


# Overload equality and less than operators

class B:
    def __init__(self, a):
        self.a = a

    def __lt__(self, other):
        if self.a < other.a:
            return "ob1 is less than ob2"
        else:
            return "ob2 is less than ob1"

    def __eq__(self, other):
        if self.a == other.a:
            return "Both are equal"
        else:
            return "Not equal"


ob1 = B(5)
ob2 = B(10)
ob3 = B(5)
if ob1 < ob2:
    print("ob1 is less than ob2")
else:
    print("ob2 is less than ob1")

if ob1 == ob3:
    print("Both are equal")
else:
    print("Both are not equal")