# If you create arrays using the array module,
# all elements of the array must be of the same type.

# Creation of array
import array as arr

# Creation of array with integer type
a = arr.array('i',[1,2,3,1,1,1,1,4,3,2])
print("a",a)

# print original array
for i in range(0,3):
    print(a[i], end=" ")
print()

# Creating an array with float type
b = arr.array('d',[2.5,3.2,3.1])
print("b", b)

# printing original array
for i in range(0,3):
    print(b[i], end=" ")
print()

# Adding elements to a array using insert
a.insert(0, 4)
print(a)

# Adding elements using append
b.append(4.4)
print(b)

# Accessing elements from the Array
print("Access elements is : ", a[0])

# Removing elements from the array
print("pop element :", a.pop(0))
print(a)

# remove() to remove 1st occurrence of 1
a.remove(4)
print(a)

# Slicing of an array
print("Slicing an array ",a[3:8])

# Searching element in a Array
# using index() to print index of 1st occurrence of 2
print(a.index(2))

# Updating elements in a array
a[5] = 100
a.append(500)
print(a)

