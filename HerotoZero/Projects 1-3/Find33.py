"""
FIND 33:
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False
"""

def has_33(l):
    for x in range(len(l)-1):
        if l[x] == 3 and l[x+1] == 3:
                return True
    return False

"""
    return [True for x in range(len(l)-1) if l[x] == 3 and l[x+1] == 3]
"""

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))