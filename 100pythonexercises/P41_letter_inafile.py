
import string

with open('Alphabets.txt','w') as f:
    for letter in string.ascii_lowercase:
        f.write(letter + '\n')

# P42 Iterating Multiple Sequences
a = [1, 2, 3]
b = (4, 5, 6)

for i,j in zip(a,b):
    print(i+j)

#P43 Letters Two by Two

import string

with open('Alpha.txt','w') as f:
    for letter1,letter2 in zip(string.ascii_lowercase[0::2],string.ascii_lowercase[1::2]):
        f.write(letter1+letter2+"\n")

#P44 three letters

import string

letters = string.ascii_lowercase + " "

slice1 = letters[0::3]
slice2 = letters[1::3]
slice3 = letters[2::3]

with open("letters.txt", "w") as file:
    for s1, s2, s3 in zip(slice1, slice2, slice3):
        file.write(s1 + s2 + s3 + "\n")

