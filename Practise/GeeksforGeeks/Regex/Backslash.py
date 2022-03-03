# For example, if you want to search for the dot(.)
# in the string then you will find that dot(.) will be treated
# as a special character as is one of the metacharacters

import re
s = "geeks.forgeeks"
# without using \
match = re.search(r'.',s)
print(match)

# Using \
match = re.search(r'\.',s)
print(match)

