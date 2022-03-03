# An OrderedDict is also a sub-class of dictionary but unlike dictionary,
# it remembers the order in which the keys were inserted.

from collections import OrderedDict
print("This is a Dict:\n")
d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

for key,value in d.items():
    print(key,value)

print("\n This is an Ordered Dict:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
for key,value in od.items():
    print(key,value)

# deleting element
od.pop('a')

# Re-inserting the same
od['a']=1

print('\n After re-inserting')
for key,value in od.items():
    print(key,value)


# Value change
od['c'] = 5
for key,value in od.items():
    print(key,value)

