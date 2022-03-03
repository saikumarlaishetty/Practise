# Arguments
def fun(x, y=20):
    print(x,y)

fun(10)
fun(50,100)

# Keyword arguments
def name(f,l):
    print(f,l)

name(f="SAI",l="Kumar")
name(l="SAI",f="Kumar")

# variable -length arguments
def v(*argv):
    for arg in argv:
        print(arg,end=" ")

v('Hello','Welcome','to','GeeksforGeeks')
print()

# variable length keyword arguments
def vl(**kwarg):
    for key,value in kwarg.items():
        print(key,value)

vl(first='Geeks',mid="is",last="geeks")

# doc string
def docstring():
    """Function is doc string"""
    pass

print(docstring.__doc__)


# Return statement
def square_value(num):
    return num*num

print(square_value(2))


# Is python pass by value or pass by reference
def my(x):
    x[0]=20

l = [10,11,12,14,15]
my(l)
print(l)

# Anonymous functions
cube2= lambda x:x*x*x
print(cube2(3))

# Nested functions
def f1():
    s = "I "
    def f2():
        print(s)
    f2()
f1()

