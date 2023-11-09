list1 = [1, 2, 3, 4, 5]
list2 = ['A', 'B', 'C', 'D', 'E']
a={}
for key in list1:
   for value in list2:
       a[key] = value
print(a)

# Actual O/P : {1: 'E', 2: 'E', 3: 'E', 4: 'E', 5: 'E'}
# Expected O/P : {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E'}


d = {}
for i in range(len(list1)):
    d[list1[i]] = list2[i]
print(d)


print(dict(zip(list1,list2)))
