# UserString is a string like container and just like
# UserDict and UserList it acts as a wrapper around string objects.
# It is used when someone wants to create
# their own strings with some modified or additional functionality.

from collections import UserString

# Create a Mutable string
class Mystring(UserString):

    # append to string
    def append(self,s):
        self.data += s

    # Remove from the string
    def remove(self,s):
        self.data = self.data.replace(s,"")

# Drivers code
s1 = Mystring("Geeks")
print("Original String:",s1.data)

s1.append("s")
print("String after appending: ",s1.data)

# Removing from string
s1.remove("e")
print("String after removing: ", s1.data)