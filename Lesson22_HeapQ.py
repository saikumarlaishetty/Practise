# Heapq module used to implemention min heap

import heapq

# Push item onto heap, maintaining the heap property
heap = []
heapq.heappush(heap,10)
print(heap)

heapq.heappush(heap,1)
print(heap)

heapq.heappush(heap,5)
print(heap)

# Heap pop
# will return the smallest value and also it will delete that from heap
# maintaining the heap property

print(heapq.heappop(heap))
print(heap)

# heapify
list1 = [1,3,5,2,4,6]
heapq.heapify(list1)
print(list1)

#heap push pop
heapq.heappushpop(list1,89)
print(list1)

# heap replace
print(heapq.heapreplace(list1,100))
print(list1)

heap = [1,20,5,4,3,6,2]
print(heapq.nsmallest(6,heap))

print(heapq.nlargest(3,heap))

# Implementation of priority queue
# tuple of priority and value
list1 = [(1,"ria"),(4,"sia"),(3,"gia")]

heapq.heapify(list1)
print(list1)

for i in range(len(list1)):
    print(heapq.heappop(list1))


