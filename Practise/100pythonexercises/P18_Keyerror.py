from pprint import pprint

d = {"Name": "John", "Surname": "Smith"}
print(d["Surname"])
# A KeyError always means Python could not find a key with the name shown next to KeyError (e.g. Smith ).

de = {"a" : 1, "b" : 2}
de["c"] = 3
print(de)

# P20 sum of all dict values
d = {"a": 1, "b": 2, "c": 3}
print(sum(d.values()))

#P21 Dictionary filtering
d = {"a": 1, "b": 2, "c": 3}
e = dict()
for x,y in d.items():
    if d[x] <= 1:
        e[x] = y
print(e)
# or
print (dict((key,value) for key,value in d.items() if value <= 1))

# P22
d = {'a':(list(range(1,11))),
     'b':(list(range(11,21))),
     'c':(list(range(21,31)))}

pprint(d)


# Access the third value of b
#from pprint import pprint

d = dict(a=list(range(1, 11)), b=list(range(11, 21)), c=list(range(21, 31)))

pprint(d["b"][2])

# P24 iternary dictionary
d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))

for key,value in d.items():
    print(key,"has value ",value)

#P25 alphabets
import string

for letter in string.ascii_lowercase:
    print(letter)