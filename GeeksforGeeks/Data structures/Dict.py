# Dictionary

dict1 = {1:"Geeks",2 :"For",3:"Geeks"}
print(dict1)

# Dict with mixed keys
Dict2 = {"Name":"Geeks",1:[1,2,3,4]}
print(Dict2)

# Creating a dict with dictionary method
Dict3 = dict({1:"One",2:"Two",3:"Three"})
print(Dict3)

# Dictionary item with each item as pair
Dict4 = dict([(1,"Okati"),(2,"Rendu")])
print(Dict4)

# Nested dictionary
Dict5 = {1:"Geeks",2:"For",3:{'A':'Welcome','B':'To','C':'Geeks'}}
print(Dict5)

# Adding elements to a dictionary
Dict6 = {}
Dict6[0] = "Geeks"
Dict6[1] = "For"

print(Dict6)

# Adding a set of value to a single key
Dict6['Value'] = [2,3,4]

# Adding nested key value to a dictionary
Dict6[5] ={'Nested':{'1':'Life','2':'Geeks'}}
print(Dict6)

# Accessing element from a dictionary
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}
print(Dict[1])

# accessing element using get
print(Dict.get(3))

Dict = {'Dict1': {1: 'Geeks'},
        'Dict2': {'Name': 'For'}}
# Accessing element using key
print(Dict['Dict1'])
print(Dict['Dict1'][1])

Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Geeks',
         'A' : {1 : 'Geeks', 2 : 'For', 3 : 'Geeks'},
         'B' : {1 : 'Geeks', 2 : 'Life'}}
# Removing elements from dictionary
# Deleting a key value
del Dict[6]

# Deleting a key from Nested dictionary
del Dict['A'][2]
print(Dict)

# Deleting a key using pop() method
print(Dict.pop(7))
print(Dict)

# Deleting an arbitary key using popitem() function
Dict = { 5 : 'Welcome', 6 : 'To', 7 : 'Geeks',
         'A' : {1 : 'Geeks', 2 : 'For', 3 : 'Geeks'},
         'B' : {1 : 'Geeks', 2 : 'Life'}}

print(Dict)
print("Popitem",Dict.popitem())
print("After pop item ", Dict)

# Using clear method
Dict.clear()
print(Dict)
