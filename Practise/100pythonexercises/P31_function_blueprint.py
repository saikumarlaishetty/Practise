def foo(a=1, b=2):
    return a + b


x = foo() - 1

# P32 Global variable
c = 1
def foo():
    return c
c = 3
print(foo())

# P33 Local variable
c = 1
def foo():
    c = 2
    return c
c = 3
print(foo())

#P34 local and global variables
def foo():
    global c
    c = 1
    return c
foo()
print(c)

#P35 string splitter

def count_words(strng):
    strng_list = strng.split()
    return strng_list

print (len(count_words("Hey there its me!")))

#P36 word counter

def count_words(txtfile):
    with open(txtfile,'r') as file:
        strng = file.read()
        #print(strng)
        strng_list = strng.split(" ")
        return len(strng_list)

input_file = 'words1.txt'
print(count_words(input_file))

#P37 Advanced word counter

def count_words1(txtfile):
    with open(txtfile,'r') as file:
        text = file.read()
        #print(strng)
        text = text.replace(","," ")
        strng_list = text.split(" ")
        return len(strng_list)

input_file = 'words2.txt'
print(count_words1(input_file))

# or
import re
def count_words1(txtfile):
    with open(txtfile,'r') as file:
        text = file.read()
        strng_list = re.split(",| ",text)
        return len(strng_list)

input_file = 'words2.txt'
print(count_words1(input_file))

# P38 Name error
import math
print(math.sqrt(9))

#P39

import math
print(math.cos(1))
# if we dont know about it use dir(math) in the python console

# typeerror
import math
print(math.pow(2,1))

