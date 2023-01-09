String1 = "Welcome to the Geeks world"
print(String1)

String2 = 'A single quote string'
print(String2)

String3 = """A triple quote string"""
print(String3)

# Characters of string
print(String1[1])
print(String1[-2])
print(String1[0])

# slicing
print(String1[3:12])

# Delete and updating from a string
#String1[3] = 'o'
#print(String1) This will give a error as strings are immutable

# Update entire string
String1 = "An entire string"
print(String1)

# A character cannot be deleted
# Whole string need to be deleted
del String1
#print(String1)

# Printing Geeks in HEX
String1 = "This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting in HEX with the use of Escape Sequences: ")
print(String1)

# Using raw String to
# ignore Escape Sequences
String1 = r"This is \x47\x65\x65\x6b\x73 in \x48\x45\x58"
print("\nPrinting Raw String in HEX Format: ")
print(String1)


# Format of strings
String1 = "{} {} {}".format('Geeks','for','Life')
print(String1)

# Positional formatting
String1 = "{1} {0} {2}".format('Geeks','for','life')

# Keyword Formatting
String1 = "{l} {f} {g}".format(f="for",g="geeks",l='one')
print(String1)


# Binary representation
String1 = "{0:b}".format(16)
print("Binary representation of 16 is ")
print(String1)

# Formatting of floats
print("\n Exponent representation  of 165.6458 is")
String1 = "{0:e}".format(165.6458)
print(String1)

# Rounding of integers
String1 = "{0:.2f}".format(1/6)
print("none-sixth is : ")
print(String1)


# String alignment
String1 = "|{:<10}|{:^10}|{:>10}|".format("Geeks","for","life")
print(String1)

# To demonstrate alignment of spaces
String1 = "\n{0:^16} was founded in {1:<4}!".format("GeeksforGeeks",2009)
print(String1)

# 