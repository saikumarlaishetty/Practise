# add() - Adds and element to the set
fruits = {'apple',"banana","cherry"}
fruits.add("orange")
print(fruits)

# clear() - Removes the elements from the set
fruits.clear()
print(fruits)


# copy() - Returns a copy of the set
fruits = {'apple',"banana","cherry"}
x = fruits.copy()
print(x)


# difference() - Returns a set containing the difference between two or more sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)


# difference_update() - Removes the items in this set that are also included in another, specified set
"""
The difference_update() method is different from the difference() method, because the difference() method returns a new 
set, without the unwanted items, and the difference_update() method removes the unwanted items from the original set.

"""

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)

# discard() - Remove the specified item
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)


# intersection() - Returns a set, that is the intersection of two ore more sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)


# intersection_update() - Removes the items in this set that are not present in other, specified set(s)
"""
The intersection_update() method is different from the intersection() method, because the intersection() method returns
a new set, without the unwanted items, and the intersection_update() method removes the unwanted items from the original set.
"""

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

# isdisjoint() - Returns whether two sets have a intersection or not
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)


# issubset() - Returns whether another set contains another set or not

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)

# pop() - Removes an element from the set
fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)


# remove() - Removes the specified element
"""
This method is different from the discard() method, because the remove() method will raise an error if the specified 
item does not exist, and the discard() method will not.
"""
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)

# symmetric_difference() - Returns a set with the symmetric differences of two sets
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)


# symmetric_difference_update() - Inserts the symmetric differences from the set and another
"""
The symmetric_difference_update() method updates the original set by removing items that are present in both sets,
 and inserting the other items.
"""

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)


# union() - Return a set containing the union of sets
"""
You can specify as many sets you want, separated by commas.
"""
# ?????????????????????? whats difference between union and update.
# Union method can specify as many sets you want, seperated by commas.
x = {"apple", "banana", "cherry","lol"}
y = {"google", "microsoft", "apple"}
z = x.union(y)
print(z)


# update() - Update the set with another set, or any other iterable
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.update(y)
print(x)

