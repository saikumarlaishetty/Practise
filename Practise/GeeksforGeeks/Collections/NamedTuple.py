from collections import namedtuple

# Declaring namedtuple()
Student = namedtuple('Student',['name','age','DOB'])
print(Student)

# Adding values
S = Student('Nandini','19','2541997')
print(S)


# Accessing using index
print(S[1])

# Accessing using name
print(S.name)

# Initializing iterable
li = ['Manjeet','19','199']

# Intializing dict
di = {'name':"Nikhil","age":19,'DOB':'1232'}

# Using make() to return namedtuple()
print(Student._make(li))
print("Using make to return ", S)

# Using _asdict() to return an OrderedDict()
print(S._asdict())
print(S)

print("The student age using index is :",end="")
print(S[1])

print("the student name using the key name is :",end="")
print(S.name)

print("The student DOB is using getattr() is :",end="")
print(getattr(S,'DOB'))

# using ** operator to return namedtuple from dictionary
print("The namedtuple instance from dict is  : ")
print(Student(**di))

# using _fields to display all the keynames of namedtuple()
print("All the fields of students are : ")
print(S._fields)

# ._replace returns a new namedtuple, it does not modify the original
print("returns a new namedtuple : ")
print(S._replace(name='Manjeet'))
# original namedtuple
print(S)
