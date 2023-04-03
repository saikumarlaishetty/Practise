# https://cisco.udemy.com/course/master-python-network-automation-for-network-engineers/learn/lecture/16768134#overview


"""

Python                 JSON
--------------------------------
dict                  object
list,tuple            array
set                   set is not JSON serializable
str                   string
int,float             number
True                  true
False                 false
None                  null


"""
# Pickle works with binary data and json works with strings

"""
You want to save a Python dictionary into a file and load it later in a Java application. What protocol should you use?

Json
AS PICKLE is python proprietary
"""


"""
You want to preserve each Python data type during serialization and deserialization. What should you use?

PICKLE

"""

"""
Your application loads (deserializes) data from untrusted sources. What should you use?

JSON
"""

"""
Which function from JSON module is used to load an encoded JSON string into a Python object?   
loads()

"""


"""
You want to save a Python set into a file on disk. What protocol should you use?
PICKLE
"""

"""
What function from JSON module is used to save Python objects to a file on disk?
dump()
"""



#################################
## Data Serialization and Deserialization with JSON
#################################
 
import json
 
# Declaring a dictionary
friends = {"Dan": (20, "London", 13242252), "Maria":[25, "Madrid", 34232424]}
 
 
# Serializing the dictionary to a text file called `friends.json
with open('friends.json', 'wt') as f:
    json.dump(friends, f, indent=4)
 
 
# Serializing the dictionary to a JSON encoded string
json_string = json.dumps(friends, indent=4)
print(json_string)
 
# Deserializing from file into a Python Object
with open('friends.json') as f:
    obj = json.load(f)
 
    print(type(obj))  # => dict
    print(obj)        # => friends = {"Dan": (20, "London", 13242252), "Maria":[25, "Madrid", 34232424]}
 
 
# Loading a JSON encoded string intro a Python Object
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
print(type(obj))    # => dict
print(obj)          # => friends = {"Dan": (20, "London", 13242252), "Maria":[25, "Madrid", 34232424]}