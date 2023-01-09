d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
    "owners":[{"firstName": "Jack", "lastName": "Petter"},
                {"firstName": "Jessy", "lastName": "Petter"}]}


print(d["employees"][1]['lastName'])

#P54
d["employees"][1]['lastName'] = 'smooth'

print(d)


#P55 Adding new employee to the dictionary

d = {"employees":[{"firstName": "John", "lastName": "Doe"},
                {"firstName": "Anna", "lastName": "Smith"},
                {"firstName": "Peter", "lastName": "Jones"}],
"owners":[{"firstName": "Jack", "lastName": "Petter"},
          {"firstName": "Jessy", "lastName": "Petter"}]}

d["employees"].append(dict(firstName="Sai" ,lastName="Kumar"))