# 1) stack with collections module
# 2) collections module we have a class called deque which is called as double ended queue
# In dequeue we can add elements on both the sides
# Stack works in LIFO order

import collections

stack = collections.deque()
print(stack)
stack.append(10)
stack.append(20)
stack.append(30)
print(stack)

print(stack.pop())
print(stack.pop())
print(stack.pop())

# Using Queue module we can implement stack
# We have a class called LifoQ

import queue
stack = queue.LifoQueue()
stack.put(10)
stack.put(20)
stack.put(30)
print(stack)

stack.get(10)
stack.get(20)
stack.get(30)
print(stack)

# To add the limit of the stack
import queue
stack =queue.LifoQueue(3)  # Now the stack can have only 3 elements

# the get and put functions take the input but it blocks until it is resolved to resolve this issue use timeout as below
stack.get(10,timeout=1)
