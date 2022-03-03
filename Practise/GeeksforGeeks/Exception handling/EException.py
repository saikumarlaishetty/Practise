a = [1, 2, 3]
try:
    print("Second element = %d " %(a[1]))
    print("Fourth element = %d " %a[3])
except:
    print("An error occurred ")


def fun(a):
    if a < 4:
        b = a/(a-3)

    print("Value of b = ", b)

try:
    fun(3)
    fun(5)
except ZeroDivisionError:
    print("ZeroDivisionError occured and Handled")
except NameError:
    print("Nameerror occured and Handled")
else:
    print("Else clause")
finally:
    print("Finally block")