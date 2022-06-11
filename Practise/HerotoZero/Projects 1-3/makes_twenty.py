"""
MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
makes_twenty(20,10) --> True
makes_twenty(12,8) --> True
makes_twenty(2,3) --> False
def makes_twenty(n1,n2):
    pass
# Check
makes_twenty(20,10)
# Check
makes_twenty(2,3)
"""

def makes_twenty(n1,n2):
    if n1== 20 or n2== 20:
        return True
    elif n1+n2 == 20:
        return True
    return False

# Check
print(makes_twenty(20,10))
# Check
print(makes_twenty(12,8))
print(makes_twenty(2,3))
