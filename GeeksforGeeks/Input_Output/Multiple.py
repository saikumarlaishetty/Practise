# Python program multiple input
# taking two input using split


x, y = input("Enter a two value: ").split()
print("Number of boys :", x)
print("Number of girls :", y)
print()


# Taking three inputs at a time
x, y, z = input("Enter a three value :").split()
print("Total number of students :", x)
print("Number of boys :", y)
print("Number of girls :", z)
print()

# Taking two inputs at a time
a, b = input("Enter a two value :").split()
print("First {} and second {}".format(a,b))
print()

# Taking multiple inputs at a time
x = list(map(int, input("Enter a multiple value : ").split()))
print("List of students :", x)

