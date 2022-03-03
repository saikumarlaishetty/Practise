print("geeks")
print("geeksforgeeks")

print("geeks", end=" ")
print("geeksforgeeks")

# array
a = [1, 2, 3, 4]

# printing a element in same
for i in range(4):
    print(a[i], end=" ")

# Printing without  new line without using loop
l = [1,2,3,4,5,6]
# using * symbol
print(*l)

# sep parameter
print('G', 'F', 'G', sep='')

# for formatting date
print('09','12','2021', sep='-')

# another example
print('pratik','geeksforgeeks', sep='@')

# sep parameter with end parameter
print('G', 'F', 'G', sep='',end=' ')

# for formatting date
print('09','12','2021', sep='-', end='\n')


# another example
print('pratik','geeksforgeeks', sep='@',end="@")
print('geeksforgeeks')