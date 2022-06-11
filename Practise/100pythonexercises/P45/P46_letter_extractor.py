import string

letters =[]
for filename in string.ascii_lowercase:
    with open(filename+'.txt','r') as file:
        letters.append(file.read().strip('\n'))

print(letters)
#or

import glob

file_list = glob.glob("letters/*.txt")
letters =[]
for filename in file_list:
    with open(filename,'r') as file:
        letters.append(file.read().strip('\n'))

print(letters)