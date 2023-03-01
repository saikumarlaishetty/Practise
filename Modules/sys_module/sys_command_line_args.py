"""
Command-line arguments are those which are passed during the calling of the
program along with the calling statement. To achieve this using
the sys module, the sys module provides a variable called sys.argv.

 It’s main purpose are:

It is a list of command-line arguments.
len(sys.argv) provides the number of command-line arguments.
sys.argv[0] is the name of the current Python script.


"""
#
# import sys
#
# n = len(sys.argv)
#
# for i in range(1,n):
#     print(sys.argv[i],end = " ")
#
#
# # Addition of numbers
# sum = 0
#
# for i in range(1,n):
#     sum += int(sys.argv[i])
#
# print("Result :",sum)



# Exiting the program

# import sys
# age = 17
# if age < 18:
#     sys.exit("Age is less than 18")
# else:
#     print("Age is not less than 18")



# Working with modules

"""
sys.path is a built-in variable within the sys module that returns the
 list of directories that the interpreter will 
search for the required module. 


"""

# import sys
# print(sys.path)

# Truncating the values of sys.path

import sys
sys.path = []

# importing pandas after removing the values
# import pandas

# sys.modules return the name of the Python modules that the current shell has imported.

import sys
print(sys.modules)


#### Reference count
"""
sys.getrefcount() method is used to get the reference count for any given object. This value is used by Python as when 
this value becomes 0, the memory for that particular value is deleted.
"""

import sys
a = 'geeks'
print(sys.getrefcount(a))

print(sys.settrace(sys.getrefcount(a)))