
# Serializing to a file
def serialize(fobj,file,type):
    if type == 'json':
        import json
        with open(file,'wt') as f:
            json.dump(fobj,f,indent=4)
    elif type == 'pickle':
        import pickle
        with open(file,'wb') as f:
            pickle.dump(fobj,f)
    else:
        print("Invalid serialization")

# Serializing to a file
def deserialize(file,type):
    if type == 'json':
        import json
        with open(file) as f:
            obj=json.load(f)
    elif type == 'pickle':
        import pickle
        with open(file,'rb') as f:
            obj =pickle.load(f)
    else:
        print("Invalid deserialization")

    print(obj)

if __name__ == '__main__':


    friends = {"Dan": (20, "London", 13242252), "Maria":[25, "Madrid", 34232424]}

    # Serializing
    serialize(friends,'a1.json','json')
    serialize(friends,'a1.dat','pickle')

    # Deserializing
    deserialize('a1.json','json')
    deserialize('a1.dat','pickle')


"""
###################
# Coding Challenge Solution
# Simply Serialization
###################
 
# Serializing to file
def serialize(obj, file, type):
    if type == 'pickle':
        import pickle
        with open(file, 'wb') as f:
            pickle.dump(obj, f)
    elif type == 'json':
        import json
        with open(file, 'w') as f:
            json.dump(obj, f)
    else:
        print('Invalid serialization. Use pickle or json!')
 
 
# Deserializing from from to Python Object
def deserialize(file, type):
    if type == 'pickle':
        import pickle
        with open(file, 'rb') as f:
            obj = pickle.load(f)
        return obj
    elif type == 'json':
        import json
        with open(file, 'r') as f:
            obj = json.load(f)
            return obj
    else:
        print('Invalid serialization. Use pickle or json!')
 
 
if __name__ == "__main__":
 
    d1 = {'a': 'x', 'b': 'y', 'c': 'z', 30: (2, 3, 'a')}
 
    # Serializing using pickle
    serialize(d1, 'a.dat', 'pickle')
 
    # Deserializing
    myDict = deserialize('a.dat', 'pickle')
    print(f'pickle: {myDict}')
 
    print('#' * 20)
 
    # serializing using pickle
    serialize(d1, 'a.json', 'json')
 
    # deserializing
    x = deserialize('a.json', 'json')
    # Notice how the tuple value was not preserved!
    print(f'json: {x}')  # {'a': 'x', 'b': 'y', 'c': 'z', '30': [2, 3, 'a']}

"""
