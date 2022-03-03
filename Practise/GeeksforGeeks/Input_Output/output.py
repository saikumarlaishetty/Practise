# print integer and float value
print("Geeks : %2d, portal : %5.2f" % (1,05.333))

print("Total students : %3d, Boys : %2d "%(240,120))

print("%7.3o" %(25))

print("%10.3E" %(356.08977))

# Python program showing format() method

# combining positional and keyword arguments
print('Number one portal is {0}, {1} and {other}'.
      format('Geeks','For',other='Geeks'))

# using format() method with number
print("Geeks: {0:2d}, portal:{1:8.2f}".format(12,00.546))

# Changing positional argument
print("Second argument :{1:3d}, first one : {0:7.2f}".format(47.42,11))

print("Geeks: {a:5d}, portal :{p:8.2f}".format(a=453, p = 59.058))

# Format used in dictionary

tab = {'geeks':4127, 'for':4098,'geek':8637678}

# using format() in dictionary
print('Geeks: {0[geeks]:d}; For : {0[for]:d}; Geeks:{0[geek]:d}'.format(tab))

data = dict(fun="GeeksForGeeks", adj="Portal")

# Using format() in dictionary
print("I love {fun} computer{adj}".format(**data))



# Formatting output using the string method

# Format a method using string() method

cstr = "I love geeksforgeeks"

# Printing the center aligned
print("Center aligned string with fillch: ")
print(cstr.center(40,"#"))

# Printing the left aligned
print("The left aligned string is :")
print(cstr.ljust(40,'-'))

# Printing the right aligned
print("The right aligned string is :")
print(cstr.rjust(40,'-'))
