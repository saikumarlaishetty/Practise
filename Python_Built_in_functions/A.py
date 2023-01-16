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




