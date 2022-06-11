import re


data = "this is the way to handle the data"

#                       1
#                     2     3     4    5
res = re.search("^((\w+)\s(\w+))(.*?)(\w+)$", data)
if res:
    print(res.group(0))
    print(res.group(1))
    print(res.group(2))
    print(res.group(3))
    print(res.group(4))
    print(res.group(5))

else:
    print("Pattern not found")
