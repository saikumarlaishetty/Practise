# Creating a set
set1 = set()
print(set1)

# Creating a set with the use of string
set1 = set("GeeksForGeeks")
print(set1)

# Creating a set with use of list
set1 = set(["Geeks","For","Geeks"])
print(set1)

# Adding element and tuple to the set
set1.add(8)  # one element at a time
set1.add(9)
set1.add((6,7)) # only tuple can be added to set but not list

print(set1)

# Adding multiple elements
for i in range(1,6):
    set1.add(i)
print(set1)

# addition of elements to the set using update function
set1 = set([4,5,(6,7)])
set1.update([10,11])
print(set1)


# Accessing element using for loop
for i in set1:
    print(i, end=" ")

# checking the element using in keyword
print("Geeks" in set1)

# Removing element from set
set1.remove(5)
set1.remove((6,7))
print(set1)

# remove element using discard method
set1.discard(11)
print(set1)

# using pop() method
set1.pop()
print(set1)

# Removing all elements from set using clear method
set1.clear()
print(set1)


