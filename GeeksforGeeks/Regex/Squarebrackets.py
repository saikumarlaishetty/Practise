# Dot(.) symbol matches only a single character except for
# the newline character (\n). For example –
#
# a.b will check for the string that contains any character
# at the place of the dot such as acb, acbd, abbb, etc
# .. will check if the string contains at least 2 characters


# Question mark(?) checks if the string before the
# question mark in the regex occurs at least once or not at all.
# For example –
#
# ab?c will be matched for the string ac, acb, dabc but will not
# be matched for abbc because there are two b. Similarly,
# it will not be matched for abdc because b is not followed by c.
import re
p = re.compile('[a-e]')
print(p.findall("Aye said Mr.Gibenson stark"))

# \d is equivalent to [0-9]
p = re.compile('\d')
print(p.findall("I went to him at 11 A.M. on 4th july 1886"))

p = re.compile('\d+')
print(p.findall("I went to him at 11 A.M on 4th july 1886"))