# Queue using module
# Collections module with dequeue class
# on left side we have appendleft and popleft
# on right side we have append and pop

# Example

import collections
q = collections.deque()

print(q)
q.appendleft(10)
q.appendleft(20)
q.appendleft(30)
print(q)

print(q.pop())
print(q.pop())
print(q.pop())


# or

q = collections.deque()

print(q)
q.append(10)
q.append(20)
q.append(30)
print(q)

print(q.popleft())
print(q.popleft())
print(q.popleft())

# To check if queue is empty or not
print(not q)

###############
##           ##
##    2      ##
## ############
# ######################################################################
# we have another  module queue with class Queue to implement queue with module
# ######################################################################


import queue
q = queue.Queue()
q.put(10)
q.put(20)
q.put(30)
# this generates a object
print(q)                   # <queue.Queue object at 0x0390FC50>

print(q.get())
print(q.get())
print(q.get())

# We can implement queue with get and put
# get(item,block=True,timeout= x secs)  is block until you get the item
# and wait till timeout
# put (item,block=True,timeout=x secs) is block until you put the item
# to the queue space is available









