# Using list comprehension

x, y = [int(x) for x in input("Enter two value :").split()]
print("First number is :", x)
print("Second number is : ",y )

# Taking three inputs at at time
x, y, z = [int(x) for x in input("Enter three value :").split()]
print("First number is :", x)
print("Second number is : ",y )

# Taking multiple inputs at a time
x = [int(x) for x in input("Enter multiple value :").split()]
print("First number is :", x)

# Taking multiple inputs at a time
x = [int(x) for x in input("Enter multiple value :").split(",")]
print("First number is :", x)