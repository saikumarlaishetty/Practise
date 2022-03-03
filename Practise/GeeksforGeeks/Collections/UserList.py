# UserList is a list like container that acts as a wrapper
# around the list objects. This is useful when someone wants to create
# their own list with some modified or additional functionality.

from collections import UserList

# Creating a List
class MyList(UserList):

    # Stop deletion from list
    def remove(self,s= None):
        raise RuntimeError("Deletion not allowed")

    # stop pop from List
    def pop(self,s=None):
        raise RuntimeError("Deletion not allowed")


L = MyList([1,2,3,4])
print("Original List")

L.append(5)
print(L)

#L.remove()
