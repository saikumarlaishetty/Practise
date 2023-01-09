list_my = []
for num in range(1,21):
    list_my.append(num)

print(list_my)

# or

my_list = range(1,21)
print(list(my_list))


# P12 _more ranges

my_range = range(1, 21)
print([x * 10 for x in my_range])  # list comprehension

# P13 _range of strings
my_range = range(1, 21)
print([str(x) for x in my_range])
# or
# map( func, iterable)
print(list(map(str,my_range)))

# P14 duplicates
a = ["1",1 , "1", 2]
print (list(set(a)))
#or
from collections import OrderedDict
a = ["1",1,"1",2]
a = list(OrderedDict.fromkeys(a))
print(a)
# or
a = ["1",1,"1",2]
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)