"""

almost_there(90) --> True
almost_there(104) --> True
almost_there(150) --> False
almost_there(209) --> True
ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

def almost_there(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

"""

def almost_there(n):
    if 90 <= n <= 110 or 190 <= n <= 210:
        return True
    else:
        return False


print(almost_there(90))
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))
