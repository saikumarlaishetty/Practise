# UserDict is a dictionary-like container that acts as a wrapper
# around the dictionary objects. This container is used when someone
# wants to create
# their own dictionary with some modified or new functionality.

# UserDict
from collections import UserDict

# Creating a Dictionary where deletion is not allowed
class MyDict(UserDict):

    # Function to stop deletion From dictionary
    def __del__(self):
        raise RuntimeError("Deletion not allowed")

    # Function to stop pop from dictionary
    def pop(self,s=None):
        raise RuntimeError("Deletion not allowed")

    # Function to stop popitem from dictionary
    def popitem(self,s=None):
        raise RuntimeError("Deletion not allowed")

d = MyDict({'a': 1,'b': 2,'c': 3})
#d.pop(1)

d1 = {'a': 1,'b': 2,'c': 3}
# Creating an UserDict
userD = UserDict(d1)
print(userD.data)

# Creating an empty Userdict
userD = UserDict()
print(userD.data)





