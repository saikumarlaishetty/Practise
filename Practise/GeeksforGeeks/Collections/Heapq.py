import heapq

li = [5,7,9,1,3]

#convert heap into list
heapq.heapify(li)

print("Created heap is :",list(li))
heapq.heappush(li,4)

print(list(li))

print("The poped and smallest elemnet is ")
print(heapq.heappop(li))

li1 = [5, 7, 9, 4, 3]

# initializing list 2
li2 = [5, 7, 9, 4, 3]

# using heapify() to convert list into heap
heapq.heapify(li1)
heapq.heapify(li2)

# using heappushpop() to push and pop items simultaneously
# pops 2
print("The popped item using heappushpop() is : ", end="")
print(heapq.heappushpop(li1, 2))

# using heapreplace() to push and pop items simultaneously
# pops 3
print("The popped item using heapreplace() is : ", end="")
print(heapq.heapreplace(li2, 2))

# initializing list
li1 = [6, 7, 9, 4, 3, 5, 8, 10, 1]

# using heapify() to convert list into heap
heapq.heapify(li1)



"""
nlargest(k, iterable, key = fun) :- This function is used to 
return the k largest elements from the iterable 
specified and satisfying the key if mentioned.

nsmallest(k, iterable, key = fun) :- This function is 
used to return the k smallest elements from the iterable 

specified and satisfying the key if mentioned."""
# using nlargest to print 3 largest numbers
# prints 10, 9 and 8
print("The 3 largest numbers in list are : ", end="")
print(heapq.nlargest(3, li1))

# using nsmallest to print 3 smallest numbers
# prints 1, 3 and 4
print("The 3 smallest numbers in list are : ", end="")
print(heapq.nsmallest(3, li1))