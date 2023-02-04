# iterate with enumerate() instead of range(len())


# This helps to get a list with only numbers greater than 0 and negative numbers to zero.
data = [1,2,-2,-4]
for i in range(len(data)):
    if data[i] < 0:
        data[i] =0

print(data)     # output [1, 2, 0, 0]

# This helps to get a list with only numbers greater than 0 and negative numbers to zero.
data = [1,2,-2,-4]
for idx,num in enumerate(data):
    if num < 0:
        data[idx] = 0

print(data)   # output [1, 2, 0, 0]

# 2) list comprehensions
squares = []
for i in range(10):
    squares.append(i*i)

print(squares)

squares = [i*i for i in range(10)]
print(squares)

# sorted list , dict and tuple
data = [3,4,5,6,2,1]
print(sorted(data,reverse=True))
print(data)

data = (1,4,3,4,2,1)
print(sorted(data))   # input list output list
                      # input tuple output list

data = [{"name": "Max", "age": 6},
        {"name": "Lisa", "age": 20},
        {"name": "Ben", "age": 9}]
print(sorted(data, key=lambda x: x["age"]))

# store unique values using set

# save memory with generators
import sys

my_list = [i for i in range(1000000)]
print(sum(my_list))
print(sys.getsizeof(my_list, 'bytes'))
my_list = (i for i in range(1000000))
print(sum(my_list))
print(sys.getsizeof(my_list, "bytes"))

# Define default values in dictionaries with .get() and .setdefault()

my_dict = {"item": "football", "price": 10.00}
print(my_dict.get("count"))  # None
print(my_dict)

print(my_dict.get("count",0))  # 0
print(my_dict.setdefault("count",0))  # None
print(my_dict)         #{'item': 'football', 'price': 10.0, 'count': None}

print(my_dict.setdefault("count",None))  # None
print(my_dict)


# 7) Count hashable objects with collection.Counter
from collections import Counter
my_list = [3,3,4,5,5,3,6,7,7,7,7,9,9,9,9,9,9,9,9]
counter = Counter(my_list)
print(counter)                # Counter({9: 8, 7: 4, 3: 3, 5: 2, 4: 1, 6: 1})
print(type(counter))
print(counter[11])             # 0 if item does not exist

most_common = counter.most_common(10)
print(most_common)

# Format strings with f strings
name = "Alex"
my_string = f"Hello {name}"
print(my_string)

i = 10
print(f"{i} squared is {i*i}")

# Concatenate strings with .join()
list_of_strings = ["Hello","Friend", "Dear"]
my_string = " ".join(list_of_strings)
print(my_string)

#Merege dictionaries
d1 = {"name":"Alex","Age":26}
d2 = {"name":"Alex","City":"HYD"}
merged_dict = {**d1,**d2}
print(merged_dict)


# simplify if statement for multiple checks
colors = ["red","blue","Yellow"]
c = "red"
if c in colors:
    print("Is main color")

    