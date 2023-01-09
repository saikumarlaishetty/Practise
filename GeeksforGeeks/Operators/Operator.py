import operator
a = 4
b = 3
print(operator.add(a,b))

print(operator.sub(a,b))

print(operator.mul(a,b))

# Python code setitem(),delitem(),getitem()

li = [1, 5, 6, 7, 8]

for i in range(0, len(li)):
    print(li[i], end=" ")

print("\r")

operator.setitem(li, 3, 3)
print(li)

operator.delitem(li, 1)
print(li)

print(operator.getitem(li, 3))

s1 = "Geeksfor"
s2 = "geeks"
print(operator.concat(s1, s2))

a = 1
b = 0

print(operator.and_(a, b))
print(operator.or_(a, b))
print(operator.xor(a, b))

print(operator.invert(a))

# == and is operator
list1 = []
list2 = []
list3 = list1

if list1 == list2:
    print("True")
else:
    print("False")
if list1 is list3:
    print("True")
else:
    print("False")

list1 = []
list2 = []
print(id(list1))
print(id(list2))

# Membership operator and identity operator
list1 = [1,2,3,4,5]
list2 = [6,7,8,9]

for item in list1:
    if item in list2:
        print("Overlapping")
else:
    print("Not overlapping")

x = 24
y = 20
list =[10,20,30,40,50]
if (y not in list):
    print("x is not present in list")
else:
    print("x is present in list")

# identity operators
x = 5
if type(x) is int:
    print("True")
else:
    print("False")
