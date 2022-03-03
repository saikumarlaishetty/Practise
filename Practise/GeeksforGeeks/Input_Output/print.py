print("Geeks for geeks \n is best for DSA content")


# This line will automatically add ** new line
print("Geeks for geeks ", end="**")
print("Welcome to GFG")

# Flush argument
import time
count_seconds = 3
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        print(i, end=">>>")
        time.sleep(1)
    else:
        print('Start')


# Same code with flush argument
import time

count_seconds = 3
for i in reversed(range(count_seconds + 1)):
    if i > 0:
        print(i, end=">>>", flush = True)
        time.sleep(1)
    else:
        print('Start')

# Separtor
b = "for"
print("Geeks", b, "Geeks")

# file argument
import io

# declare a dummy file
dummy_file = io.StringIO()

# add message to the dummy file
print("Hello Geeks!! ", file=dummy_file)

# get the value from dummy file
dummy_file.getvalue()


# print()
print("GFG")

x = 5
print("x =  ",x)

print('G', 'F','G', sep='')

print("Python", end = '@')
print("GeeksforGeeks")


