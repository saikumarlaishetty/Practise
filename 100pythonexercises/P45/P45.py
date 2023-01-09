

#One File per Letter

import string
import os

if not os._exists('letters'):
    os.makedirs("letters")

for letter in string.ascii_lowercase:
    with open("letters/"+letter+'.txt','w') as f:
        f.write(letter)

