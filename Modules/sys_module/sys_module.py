"""
The sys module in Python provides various functions and variables that are used to
manipulate different parts of the Python runtime environment.

It allows operating on the interpreter as it provides access to the variables
and functions that interact strongly with the interpreter.

Let’s consider the below example.

"""

import sys

#print(sys.version)


# Input and output using sys

"""
The sys modules provide variables for better control over input or output. 
We can even redirect the input and output to other devices. 
This can be done using three variables – 
 
stdin
stdout
stderr
"""

# stdin

"""
It can be used to get input from the command line directly. It is used for standard input. It internally calls the input() method. 
It, also, automatically adds ‘\n’ after each sentence.

"""

# import sys
#
# for line in sys.stdin:
#     if 'q' == line.rstrip():
#         break
#     print(f'Input : {line}')
#
# print("Exit")



"""
stdout :
stdout is used to display output directly to the screen console


"""

import sys

sys.stdout.write('Geeks')


"""

stderr: Whenever an exception occurs in Python it is written to sys.stderr. 

"""
#
# import sys
#
#
# def print_to_stderr(*a):
#     # Here a is the array holding the objects
#     # passed as the argument of the function
#     print(*a, file=sys.stderr)
#
#
# print_to_stderr("Hello World")
