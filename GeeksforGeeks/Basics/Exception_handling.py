# initializing number
a = 4
b = 0

# No exception Exception raise by try block
try:
    k = a//b  # raises divide by zero exception
    print(k)

    # handles zero division exception
except ZeroDivisionError:
    print("Can't divide by zero")

finally:
    # This block is always executed
    # regardless of exception generation
    print("This is always executed")


# assert keyword
# using assert to check for 0
print("The value of a/b is : ")
assert b != 0, "Divide by 0 error"
print(a/b)

