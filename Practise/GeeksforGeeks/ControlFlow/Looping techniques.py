# code to demonstrate of ennumerate()
for key,value in enumerate(['The','Big','Bang','Theory']):
    print(key,value)

# Using zip
q = ['name','color','shape']
a = ['apple','red','circle','key']
for i,j in zip(q,a):
    print(i," = ",j)

dict1 = { "geeks" : "for", "only" : "geeks" }
for i, j in dict1.items():
    print(i,j)

# Using sorted
l = [1,2,3,1,2,1,1,56,78,95,3,5]
print("Sorted list", sorted(l)) # list is sorted
print(l)  # list is same as above l
print(set(sorted(l))) # used to remove duplicates

print("Reversed", reversed(l))