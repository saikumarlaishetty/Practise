"""
SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order
 spy_game([1,2,4,0,0,7,5]) --> True
 spy_game([1,0,2,4,0,5,7]) --> True
 spy_game([1,7,2,0,4,5,0]) --> False
"""

def spy_game(nums):
    l = []
    for x in nums:
        if x == 0 or x == 7:
            l.append(x)
        continue
    #print(l)
    for x in range(len(l)-2):
        if l[x] == 0 and l[x+1] == 0 and l[x+2] == 7:
            return True
    return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))