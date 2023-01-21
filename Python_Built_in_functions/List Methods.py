"""
Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.


"""

# append() - Adds an element at the end of the list
fruits = ["apple","banana","cherry"]
fruits.append("orange")
print(fruits)

# clear() - Removes all the elements from the list
fruits.clear()
print(fruits)

# copy() - Returns a copy of the list
fruits = ["apple","banana","cherry"]
seasonal_fruits = fruits.copy()
print(seasonal_fruits)

# count() - Returns the number of elements with the specified value
print(fruits.count("Orange"))
print(fruits.count("banana"))

# extend() - Add the elements of a list( or any iterable), to the end of the current lists
some_fruits = ["kiwi"]
fruits.extend(some_fruits)
print(fruits)


# index() - Returns the index of the first element with the specified value
fruits = ["apple","banana","cherry","kiwi","banana","Orange"]
print(fruits.index("banana"))

# insert() - Adds an element at the specified position
print(fruits.insert(0,"Tomato"))   # returns None
print(fruits)

# pop() - Removes the first item with the specified value
print(fruits.pop(0))

# remove() - Removes the first item with the specified value
print(fruits.remove("cherry"))
#print(fruits.remove("cherry"))
print(fruits)

# reverse() - Reverses the order of the list
print(fruits.reverse())  # None
print(fruits)

# sort() - Sorts the list
# list.sort(reverse=True|False, key=myFunc)
# reverse --> Optional. reverse=True will sort the list descending. Default is reverse=False
print(fruits.sort())

print(fruits)

# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(reverse=True, key=myFunc)