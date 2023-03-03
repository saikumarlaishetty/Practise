"""
A Regular Expressions (RegEx) is a special sequence of characters that uses a search pattern to find a string or set of strings.

"""

import re

s = 'GeeksforGeeks portal : A computer science portal for geeks'

match = re.search(r'portal',s)    # r stands for raw not regex

"""
The raw string is slightly different from a regular string, it won’t interpret the \ character as an escape character. This is because the 
regular expression engine uses \ character for its own escaping purpose.
"""

print(match)                         #  <re.Match object; span=(34, 40), match='portal'>

print('start Index: ',match.start())     # start Index:  34
print('End Index :',match.end())         # End Index : 40

"""
\    - used to drop the special meaning of character following it
[]   - Represent a character class
^    - Matches the beginning
$    - Matches the end
.    - Matches any character except newline
|    - Means OR ( Matches with any of the characters seperated it).
?    - Matches zero or one occurrence
*    - Any number of occurrences (including 0 occurrences).
+    - one or more occurrences
{}   - Indicate the number of occurrences of a preceding regex to match
()   - Enclose a group of regex

"""

################################################
#####      / - Backslash
################################################

import re
s = 'geeks.forgeeks'

# without using /
match = re.search(r'.',s)
print(match)         # <re.Match object; span=(0, 1), match='g'>

match = re.search(r'\.',s)
print(match)                 # <re.Match object; span=(5, 6), match='.'>



###############################################
#####    SQUARE BRACKETS
###############################################

import re

string = "The quick brown fox jumps over the lazy dog"
pattern = "[a-m]"

result = re.findall(pattern,string)

print(result)    # ['h', 'e', 'i', 'c', 'k', 'b', 'f', 'j', 'm', 'e', 'h', 'e', 'l', 'a', 'd', 'g']

###############################################
#####    ^ caret
###############################################

regex = r'^The'
strings = ['The quick brown fox', 'The lazy dog', 'A quick brown fox']

for string in strings:
    if re.match(regex,string):
        print(f'Matched : {string}')
    else:
        print(f'Not matched : {string}')

"""
Matched : The quick brown fox
Matched : The lazy dog
Not matched : A quick brown fox
"""

# Dollar

import re

string = "Hello World!"
pattern = r'World!$'

match = re.search(pattern,string)
if match:
    print("Match found")
else:
    print("Match not found")    # Match found


# .DOT

# Dot symbol matches only a single character except for the new line character

import re

string = "The quick brown fox jumps over the lazy dog."
pattern = r"brown.fox"

match = re.search(pattern, string)
print(match)

if match:
    print("Match found!")
else:
    print("Match not found.")


########
"""
re.findall()
Return all non-overlapping matches of pattern in string, as a list of strings. 
The string is scanned left-to-right, and 
matches are returned in the order found.
"""

import re

string = """Hello my Number is 123456789 and
            my friend's number is 987654321"""

# A sample regular expression to find digits.
regex = '\d+'

match = re.findall(regex, string)
print(match)          # ['123456789', '987654321']


#######################
# COMPILE
"""
Regular expressions are compiled into pattern objects, which have methods for various operations such as searching for
pattern matches or performing string substitutions. 
"""

# compile() creates regular expression
# character class [a-e],
# which is equivalent to [abcde].
# class [abcde] will match with string with
# 'a', 'b', 'c', 'd', 'e'.
p = re.compile('[a-e]')

# findall() searches for the Regular Expression
# and return a list upon finding
print(p.findall("Aye, said Mr. Gibenson Stark"))           # ['e', 'a', 'd', 'b', 'e', 'a']


## Example 2

import re

# \d is equivalent to [0-9].
p = re.compile('\d')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))   # ['1', '1', '4', '1', '8', '8', '6']

# \d+ will match a group on [0-9], group
# of one or greater size
p = re.compile('\d+')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))   # ['11', '4', '1886']



import re
# '*' replaces the no. of occurrence
# of a character.
p = re.compile('ab*')
print(p.findall("ababbaabbb"))         # ['ab', 'abb', 'a', 'abbb']


#################
# re.split()
# re.split(pattern, string, maxsplit=0, flags=0)
#################

"""
Split string by the occurrences of a character or a pattern, upon finding that pattern, the remaining characters from
the string are returned as part of the resulting list

"""

from re import split

# '\W+' denotes Non-Alphanumeric Characters
# or group of characters Upon finding ','
# or whitespace ' ', the split(), splits the
# string from that point
print(split('\W+', 'Words, words , Words'))       # ['Words', 'words', 'Words']
print(split('\W+', "Word's words Words"))         # ['Word', 's', 'words', 'Words']

# Here ':', ' ' ,',' are not AlphaNumeric thus,
# the point where splitting occurs
print(split('\W+', 'On 12th Jan 2016, at 11:02 AM'))     # ['On', '12th', 'Jan', '2016', 'at', '11', '02', 'A

# '\d+' denotes Numeric Characters or group of
# characters Splitting occurs at '12', '2016',
# '11', '02' only
print(split('\d+', 'On 12th Jan 2016, at 11:02 AM'))   # ['On ', 'th Jan ', ', at ', ':', ' AM']


######################################################################

import re

# Splitting will occurs only once, at
# '12', returned list will have length 2
print(re.split('\d+', 'On 12th Jan 2016, at 11:02 AM', 1))      # ['On ', 'th Jan 2016, at 11:02 AM']

# 'Boy' and 'boy' will be treated same when
# flags = re.IGNORECASE
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here', flags=re.IGNORECASE))    # ['', 'y, ', 'oy oh ', 'oy, ', 'om', ' h', 'r', '']
print(re.split('[a-f]+', 'Aey, Boy oh boy, come here'))                          # ['A', 'y, Boy oh ', 'oy, ', 'om', ' h', 'r', '']




###############################################
#### re.sub()
##############################################

"""
The ‘sub’ in the function stands for SubString, a certain regular expression 
pattern is searched in the given string(3rd parameter), and upon finding the 
substring pattern is replaced by repl(2nd parameter), count checks and maintains 
the number of times this occurs. 

Syntax:

re.sub(pattern, repl, string, count=0, flags=0)

"""

import re

print(re.sub('ub','~*','Subject has Uber booked already',flags=re.IGNORECASE))
# S~*ject has ~*er booked already


# Consider the Case Sensitivity, 'Ub' in
# "Uber", will not be replaced.
print(re.sub('ub', '~*', 'Subject has Uber booked already'))
# S~*ject has Uber booked already

# As count has been given value 1, the maximum
# times replacement occurs is 1
print(re.sub('ub', '~*', 'Subject has Uber booked already',
             count=1, flags=re.IGNORECASE))
# S~*ject has Uber booked already


# 'r' before the pattern denotes RE, \s is for
# start and end of a String.
print(re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE)  )
# Baked Beans & Spam



####################
# re.subn()
###################
"""
subn() is similar to sub() in all ways, except in its way of providing output.
It returns a tuple with a count of the 
total of replacement and the new string rather than just the string. 

Syntax:

 re.subn(pattern, repl, string, count=0, flags=0)

"""

import re

print(re.subn('ub', '~*', 'Subject has Uber booked already'))

t = re.subn('ub', '~*', 'Subject has Uber booked already',
            flags=re.IGNORECASE)
print(t)   # ('S~*ject has Uber booked already', 1)
         # ('S~*ject has ~*er booked already', 2)
print(len(t))   # 2

# This will give same output as sub() would have
print(t[0])         # S~*ject has ~*er booked already



##########################################
###### re.escape()
#########################################
"""
Returns string with all non-alphanumerics backslashed, 
this is useful if you want to match an arbitrary literal string that may have 
regular expression metacharacters in it.

Syntax:

re.escape(string)
"""

import re

# escape() returns a string with BackSlash '\',
# before every Non-Alphanumeric Character
# In 1st case only ' ', is not alphanumeric
# In 2nd case, ' ', caret '^', '-', '[]', '\'
# are not alphanumeric
print(re.escape("This is Awesome even 1 AM"))
print(re.escape("I Asked what is this [a-9], he said \t ^WoW"))

"""
Output
This\ is \ Awesome\ even\ 1\ AM
I\ Asked\ what\ is \ this\ \[a\-9\]\, \ he\ said\ \    \ \ ^ WoW
"""


###############################################
##### re.search()
#############################################
"""
re.search()
This method either returns None (if the pattern doesn’t match), 
or a re.MatchObject contains information about the matching part of the string.
This method stops after the first match, so this is best suited for testing a 
regular expression more than extracting data.

"""

# A Python program to demonstrate working of re.match().
import re

# Lets use a regular expression to match a date string
# in the form of Month name followed by day number
regex = r"([a-zA-Z]+) (\d+)"

match = re.search(regex, "I was born on June 24")

if match != None:

    # We reach here when the expression "([a-zA-Z]+) (\d+)"
    # matches the date string.

    # This will print [14, 21), since it matches at index 14
    # and ends at 21.
    print("Match at index %s, %s" % (match.start(), match.end()))

    # We use group() method to get all the matches and
    # captured groups. The groups contain the matched values.
    # In particular:
    # match.group(0) always returns the fully matched string
    # match.group(1) match.group(2), ... return the capture
    # groups in order from left to right in the input string
    # match.group() is equivalent to match.group(0)

    # So this will print "June 24"
    print("Full match: %s" % (match.group(0)))

    # So this will print "June"
    print("Month: %s" % (match.group(1)))

    # So this will print "24"
    print("Day: %s" % (match.group(2)))

else:
    print("The regex pattern does not match.")
"""
Output :

Match at index 14, 21
Full match: June 24
Month: June
Day: 24

"""

###################################
### Match Object
##################################

"""
Match Object
A Match object contains all the information about the search and the result and
if there is no match found then None will be returned.
Let’s see some of the commonly used methods and attributes of the match object.

"""

import re

s = "Welcome to GeeksForGeeks"

# here x is the match object
res = re.search(r"\bG", s)

print(res.re)               # re.compile('\\bG')
print(res.string)           # Welcome to GeeksForGeeks

"""
Getting index of matched object
start() method returns the starting index of the matched substring
end() method returns the ending index of the matched substring
span() method returns a tuple containing the starting and the ending index of the matched substring
Example: Getting index of matched object 

"""

import re

s = "Welcome to GeeksForGeeks"

# here x is the match object
res = re.search(r"\bGee", s)

print(res.start())
print(res.end())
print(res.span())

print(res)

"""
Getting matched substring
group() method returns the part of the string for which the patterns match. See the below example for a better understanding.

Example: Getting matched substring 

"""
import re

s = "Welcome to GeeksForGeeks"

# here x is the match object
res = re.search(r"\D{2} t", s)

print(res.group())               # me t


