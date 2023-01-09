class CSStudent:
    # class variable
    stream = 'cse'
    def __init__(self,name,roll):
       # instance variable
        self.name = name
        self.roll = roll


# objects of CSStudent class
a = CSStudent('Geek',1)
b = CSStudent('Nerd',2)

print(a.stream,"a.stream")
print(b.stream,"b.stream")
print(a.name,"a.name")
print(b.name,"b.name")
print(a.roll,"a.roll")
print(b.roll,"b.roll")

# Class variables can be accessed using class name also
print(CSStudent.stream)

# Now if we change the stream for just "a" it won't be changed for b
a.stream = 'ece'
print("Changed ",a.stream)
print(b.stream)

# To change the stream for all the instances of the class we can
# change it directly from the class
CSStudent.stream = 'mech'

print(a.stream)
print(CSStudent.stream)
print(b.stream)