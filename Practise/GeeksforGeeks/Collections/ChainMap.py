from collections import ChainMap

d1 = {'a':1, 'b':2}
d2 = {'b':3, 'd':4}
d3 = {'e':5,'f':6}

# define the chainmap
c = ChainMap(d1,d2,d3)

print("All the chain map contents are :",c.maps)

# Accessing keys and values from ChainMap

print(c['a'])

print("All the chain map values are")
print(list(c.values()))

print("All the chain map keys are")
print(list(c.keys()))

# Adding new dictionary
# using new_Child() to add new dictionary
chain1 = c.new_child(d3)
print(chain1)

# displaying value associated with b before reversing
print("Value associated with b before reversing is : ", end="")
print(chain1['b'])

# reversing the ChainMap
chain1.maps = reversed(chain1.maps)

# displaying value associated with b after reversing
print("Value associated with b after reversing is : ", end="")
print(chain1['b'])