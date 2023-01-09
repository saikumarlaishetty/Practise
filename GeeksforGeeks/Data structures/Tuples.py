# Tuple
T1 = ("Geeks","For")
print(T1)

# Creating a tuple with the use of string
list1 = [1,1,2,3,4]
print(tuple(list1))

# Creating a tuple with the use of builtin function
T2 = tuple("Geeking")
print(T2)

# Tuple with mixed data type
T3 = (5,"Welcome")
print(T3)

# Tuple with nested tuples
T4 = (T2, T3)
print(T4)

# Accessing tuple with indexing
Tuple1 = tuple("Geeks")
print(Tuple1[1])

# Tuple unpacking
Tuple1 = ("Geeks","For","Geeks")
a,b,c = Tuple1
print(a)
print(b)
print(c)


# Concatenation
Tuple3 = Tuple1 + T2
print(Tuple3)

# Slicing of tuple
Tuple1 = tuple("GeeksforGeeks")
print("Removal of first element",Tuple1[1:])

# Reversing the tuple
print(Tuple1[::-1])

# printing elements of a range
print(Tuple1[4:9])

# Deleting a tuple
del T2

