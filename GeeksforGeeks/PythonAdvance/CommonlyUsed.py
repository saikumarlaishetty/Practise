import os
print(os.name)

"""
try :
    filename = 'GFG.txt'
    f = open(filename,'rU')
    text = f.read()
    f.close()

except IOError:
    print("Problem reading :" + filename )"""

result = os.path.exists("filename")
print(result)

