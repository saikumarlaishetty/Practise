class Dog:
    # class variable
    animal = 'Dog'

    def __init__(self,breed,color):
        # Instance variable
        self.breed = breed
        self.color = color


Rodger = Dog("Pug","Brown")
Buzo = Dog("Bulldog","black")

print("Rodger Details:")
print("Rodger is a ", Rodger.animal)
print("Breed :", Rodger.breed)
print("Color :", Rodger.color)

print("Buzo details :")
print("Buzo is a ",Buzo.animal)
print("Breed :" , Buzo.breed)
print("Color:",Buzo.color)

print("Accessing class variable using class name")
print(Dog.animal)
Dog.animal = 'tret'
print(Dog.animal)

