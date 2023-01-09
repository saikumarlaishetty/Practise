# Priority  queue is assigned based on the value itself or
# use a tuple with a value to assign the priority

# we can have lowest number highest priority or
# we can have highest number lowest priority

# Implementation of queue 1) list 2)priority queue

# implentation of lowest value high priority
q = []
q.append(10)
q.append(40)
q.sort()
q.append(20)
q.sort()
print(q)
print(q.pop(0))
print(q.pop(0))
print(q.pop(0))

# the above method is not the best method to implement priority queue
# the bet method is to implement using binary heap

# implement using priority queue

import queue
q = queue.PriorityQueue()
q.put(10)
q.put(60)
q.put(20)
q.put(40)
q.put(40)
print(q.get())
print(q.get())
print(q.get())
print(q.get())

# Add the tuple as priority for the item
# this is the method for highest value highest priority
q = []
q.append((1,"alexa"))
q.append((4,"alex"))
q.append((2,"al"))
q.sort(reverse=True)
print(q)

print(q.pop(0))
print(q.pop(0))
print(q.pop(0))



# To do
# Need to learn how to implement queue with binary heap





