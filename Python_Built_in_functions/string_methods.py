
"""
Note :

All string methods returns new values. They do not change the original string.

"""

word = "saikumar Is a software engineer \t tab"

# capitalize() -  Converts the first character to upper case
new_word = word.capitalize()
print(new_word)


# casefold() - converts string to lower case

new_word = word.casefold()
print(new_word)

# center() - returns a centered string
new_word = word.center(40,'w')
print(new_word)


# count() - Returns the number of times a specified value occurs in a string
new_word = word.count('a')
print(new_word)


# encode() - Returns an encoded version of the string
new_word = word.encode()
print(new_word)

# endswith() - Returns true if the string ends with the specified value
new_word = word.endswith('do')
print(new_word)

# expandtabs() - Sets the tab size of the string
new_word = word.expandtabs(10)
print(new_word)


# find() - Searches the string for a specified value and returns the position of where it was found
new_word = word.find('neer')
print(new_word)


# format() - Formats specified values in a string
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

# format_map() - Formats specified values in a string



# index() - Searches the string for a specified value and returns the position of where it was found.

new_word = word.find('neer')
print(new_word)



"""
Difference between find() and index() ?????????????????????

The find() method returns -1 if the value is not found.

The index() method raises an exception if the value is not found.

The find() method is almost the same as the index() method, the only difference is that the index() 
method raises an exception if the value is not found.
"""


# isalnum() - Returns True if all the characters in the string are alphanumeric
new_word = word.isalnum()
print(new_word)



# isalpha() - Returns True if all the characters in the string are in the alphabet
new_word = word.isalpha()
print(new_word)

# isascii() - Returns True if all the characters in the string are ascii characters
new_word = word.isascii()
print(new_word)


# isdecimal() - Returns True if all the characters in the string are decimals
new_word = word.isdecimal()
print(new_word)


# isdigit() - Returns True if all the characters in the string are digits
new_word = word.isdigit()
print(new_word)


# isidentifier() - Returns True if the string is an identifier
# A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_).
# A valid identifier cannot start with a number, or contain any spaces.
new_word = word.isidentifier()
print(new_word)


# islower() - Returns True if all the characters in the string
new_word = word.islower()
print(new_word)


# isnumeric() - Returns True if all the characters in the string in numeric
new_word = word.isnumeric()
print(new_word)


# islower() - Returns True if all the characters in the string are lower case
new_word = word.islower()
print(new_word)


# isprintable() - Returns True if all the characters in the string are printable
new_word = word.isprintable()
print(new_word)

# isspace() - Returns True if all the characters in the string are whitespaces
new_word = word.isspace()
print(new_word)


# istitle() - Returns True if all the string follows the rules of a title
new_word = word.istitle()
print(new_word)


# isupper() - Returns True if all the characters in the string are upper case
new_word = word.isupper()
print(new_word)


# join() - Converts the elements of an iterable into a string
myTuple = ("John", "Peter", "Vicky")
x = " ".join(myTuple)
print(x)

# ljust() - Returns a left justified version of a string
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")

# lower() - converts a string into a lower case
new_word = word.lower()
print(new_word)

# lstrip() - Returns a left trim version of the string
txt = "     banana     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")


# maketrans() - Returns a translation table to be used in translations
txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))


# partition() - Returns a tuple where the string in parted into three parts
txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)


# replace() - Returns a string where specified value is replaced with a specified value
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)

# rfind() - Searches the string for a specified value and returns the last position of where it was found.
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)

# rindex() - Searches the string for a specified value and returns the last position of where it was found.
txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)


# rjust() - Returns a right justified version of the string
txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.")


# rpartition() - Returns a tuple where string is parted into three parts
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)

# rsplit() - Splits the string at the specified seperator and returns a list
txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)

# rstrip() - Returns a right trim version of the string
txt = "     banana     "
x = txt.rstrip()
print("of all fruits", x, "is my favorite")


# split() - Splits the string at the specified separator, and returns a list
txt = "welcome to the jungle"
x = txt.split()
print(x)

# splitlines() - Splits the string at line breaks and returns a list
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)

# startswith() - Returns true if the string starts with the specified value
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)

# strip() - Returns a trimmed version of the string
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is my favorite")


# swapcase() - Swaps cases, lower case becomes uppercase and viceversa
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)

# title() - Converts the first character of each word to the upper case
txt = "Welcome to my world"
x = txt.title()
print(x)

# translate() - Returns a translated string
#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))

# upper() - Converts a string into upper case
txt = "Hello my friends"
x = txt.upper()
print(x)

# zfill() - Fills the string with a specified number of 0 values at the beginning.
txt = "50"
x = txt.zfill(10)
print(x)