"""
Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
Original String :  Hello Mr. Rogers, how are you this fine Tuesday?
No. of Upper case characters :  4
No. of Lower case Characters :  33

"""

"""
def up_low(s):
    u = []
    l = []
    li = s.split()
    for x in li:
        for y in x:
            if y.isupper():
                u.append(y)
            if y.islower():
                l.append(y)
    print("No. of Upper case characters :", len(u))
    print("No. of Lower case Characters :", len(l))


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)

"""

def up_low(s):
    d={"upper":0, "lower":0}
    for c in s:
        print(c)
        if c.isupper():
            d["upper"]+=1
        elif c.islower():
            d["lower"]+=1
        else:
            pass
    print("Original String : ", s)
    print("No. of Upper case characters : ", d["upper"])
    print("No. of Lower case Characters : ", d["lower"])
s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)