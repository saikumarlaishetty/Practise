#$  A Container is an object that is used to store
# different objects and provide a way to access the contained
# objects and iterate over them.
# Some of the built-in containers are Tuple, List, Dictionary,

# Different ways to create counter
from collections import Counter

# With sequence of items
print(Counter(['B','B','A','B','C','A','B','B','A','C']))

# With dictionary
print(Counter({'B': 5, 'A': 3, 'C': 2}))

# with keyword arguments
print(Counter(A=3,B=5,C=2))

# Create an empty counter in the following manner
coun = Counter()

# update the counter
coun.update([1,2,3,1,2,1,1,2])
print(coun)

c1 = Counter(A=4,B=3,C=10)
c2 = Counter(A=10,B=3,C=4)
c1.subtract(c2)
print(c1)

# Create a list
z = ['blue','red','blue','yellow']
print(Counter(z))
