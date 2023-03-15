#################################
## Data Serialization and Deserialization with JSON
#################################

import json

# Declaring the dictionary
friends = {"Dan":(20,"London",12345),"Meria":(25,"Paris",67909)}

# Serializing the dictionary to a text file called `friends.json'
with open('try.json','wt') as f:
    json.dump(friends,f,indent=4)

# Serializing the dictionary to a JSON encoded string
json_string = json.dumps(friends,indent=4)
print(json_string)

# Deserialzing from file into a python object
with open('try.json') as f:
    obj = json.load(f)

    print(type(obj))
    print(obj)


# Loading a JSON encoded string into a python object
json_string = """{
    "Dan": [
        20,
        "London",
        13242252
    ],
    "Maria": [
        25,
        "Madrid",
        34232424
    ]
}"""

obj = json.loads(json_string)
print(type(obj))
print(obj)




