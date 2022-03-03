import re
s = "GeeksforGeeks: A computer science portal for geeks"
match = re.search(r'portal',s)
print(match.start())
print(match.end())

# Note: Here r character (r’portal’) stands for raw, not regex.
# The raw string is slightly different from a regular string,
# it won’t interpret the \ character as an escape character.
# This is because the regular expression engine uses \ character
# for its own escaping purpose.