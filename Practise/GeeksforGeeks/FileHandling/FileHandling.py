# f = open(filename,mode)

f = open('geek.txt', 'r')

# for each in f:
#    print(each)

# read mode
# print(f.read())

# read mode character wise
print(f.read(5))

# write mode

file = open('geek.txt','w')
file.write("This is the write command")
file.close()

# append mode
file = open('geek.txt','a')
file.write('This will add this line')
file.close()


# Python code to illustrate with()
with open("geek.txt") as file:
    data = file.read()

# Python code to illustrate with() write
with open("geek.txt", 'w') as f:
    f.write("This is a python code with write mode with()")

with open("geek.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)

# seek(n) takes the file handle to the nth
# bite from the beginning.
file.seek(0)

# there is no need to call file.close() when using with statement.
# The with statement itself ensures proper acquisition and
# release of resources.