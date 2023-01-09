# Deque (Doubly Ended Queue) is the optimized list for quicker
# append and pop operations from both sides of the container.

from collections import deque

# Declaring deque
queue = deque(['name','age','DOB'])
print(queue)

# initializing deque
de = deque([1,2,3])

# Using append to insert element at right end
de.append(4)

# Printing modified deque
print(de)

# Using appendleft() to insert element
de.appendleft(6)
print(de)

# Removing elements using pop
de.pop()
print(de)

# using popleft() to delete element
de.popleft()
print(de)

import collections
de = collections.deque([1,2,3,3,4,2,4])
print("number 4 first occurs at a position",de.index(4,2,5))
de.insert(4,3)
print(de)
print("count of 3 in deque is ",de.count(3))
de.remove(3)
print("Deleting first occurence of 3 is: ",de )

# using extend() to add numbers to right end
# adds 4,5,6 to right end
de.extend([4, 5, 6])

# printing modified deque
print("The deque after extending deque at end is : ")
print(de)

# using extendleft() to add numbers to left end
# adds 7,8,9 to right end
de.extendleft([7, 8, 9])

# printing modified deque
print("The deque after extending deque at beginning is : ")
print(de)

# using rotate() to rotate the deque
# rotates by 3 to left
de.rotate(-3)

# printing modified deque
print("The deque after rotating deque is : ")
print(de)

# using reverse() to reverse the deque
de.reverse()

# printing modified deque
print("The deque after reversing deque is : ")
print(de)

