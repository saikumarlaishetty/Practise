# built in polymorphic
print(len("Geeks"))

print(len([10,20,30]))


# User defined
def add(x,y,z=0):
    return x+y+z

print(add(2,3))
print(add(2,3,4))

# polymorphism with class methods
class India():
    def capital(self):
        print("New Delhi is the capital of INDIA")
    def language(self):
        print("Hindi is the most widely spoken language of INDIA")
    def type(self):
        print("India is a developing country")

class USA():
    def capital(self):
        print("Washington is the capital of USA")
    def language(self):
        print("English is the primary language of USA")
    def type(self):
        print("USA is a developed country")

obj_ind = India()
obj_usa = USA()
for country in (obj_ind,obj_usa):
    country.capital()
    country.language()
    country.type()
    