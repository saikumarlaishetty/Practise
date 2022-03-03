# A DefaultDict is also a sub-class to dictionary. It is used to provide some default values for the
# key that does not exist and never raises a KeyError.

from collections import defaultdict

# Defaulting the dict
d = defaultdict(int)
L = [1,2,3,4,2,4,1,2]

# for keeping the count
for i in L:
    d[i] += 1

print(d)

# list
dl = defaultdict(list)
for i in range(5):
    dl[i].append(i)

print("Dictionary with values as list: ")
print(dl)

def def_value():
    return "Not Present"

d = defaultdict(def_value)
d["a"] = 1
d["b"] = 2

print(d["a"])
print(d["b"])
print(d["c"])

print(d['a'])
print(d.__missing__(1))

