import re

name = "varun"
res = re.search("^varun", name )
print(res)


data = "sample text was used to edit"

res = re.sub("[aeiou]", "*", data)

print(res)

data = "10,20-30 40:50|60 70"

flst = re.split("\W", data)

print(flst)

data = "hello 10 then 20 also 50 then b60 70"

flst = re.findall("\d+", data)

print(flst)
