
# clear() - Removes all the elements from the dictionary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.clear()
print(car)

# copy() - Returns a copy of the dicitonary
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car2 = car.copy()
print(car2)

# fromkeys() - Returns a dictionary with the specified keys and value
"""

Parameter	Description
keys	Required. An iterable specifying the keys of the new dictionary
value	Optional. The value for all keys. Default value is None
"""

x = ('key1', 'key2', 'key3')
y = 0

thisdict = dict.fromkeys(x,y)
print(thisdict)


# get() - Returns the value of the specified key
print(car.get('year'))


# items() - Returns a list containing a tuple for each key value pair
print(car.items())


# keys() - Returns a list containing the dictionary keys
print(car.keys())


# pop() - Removes the element with the specified key
print(car.pop("year"))
print(car)


# popitem() - Removes the last inserted key-value pair
print(car.popitem())


# setdefault() - Returns the value of the specified key. If the key does not exist: insert the key, with the specidfied value
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car)


# update() - Updates the dictionary with the specified key-value pairs
print(car.update({"color":"Red"}))
print(car)

# Values()- Returns a list of all the values in the dictonary
print(car.values())

