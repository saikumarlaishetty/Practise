"""
MASTER YODA: Given a sentence, return a sentence with the words reversed
master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We'

Note: The .join() method may be useful here. The .join() method allows you to join together strings in a list with some connector string. For example, some uses of the .join() method:
 "--".join(['a','b','c'])
 'a--b--c'

This means if you had a list of words you wanted to turn back into a sentence, you could just join them with a single space string:

 " ".join(['Hello','world'])
 "Hello world"
def master_yoda(text):
    pass
# Check
master_yoda('I am home')
# Check
master_yoda('We are ready')

def master_yoda(text):
    return ' '.join(text.split()[::-1])
"""

def master_yoda(text):
    l = text.split()
    return " ".join(l[::-1])
# Check
print(master_yoda('I am home'))
# Check
print(master_yoda('We are ready'))