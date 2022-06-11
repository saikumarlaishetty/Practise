"""
SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting
with a 6 and extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.

summer_69([1, 3, 5]) --> 9
summer_69([4, 5, 6, 7, 8, 9]) --> 9
summer_69([2, 1, 6, 9, 11]) --> 14
"""

def summer_69(arr):
    l = []
    flag = 0
    if arr is None:
        return 0
    for x in arr:
        if x == 6:
            flag = 1
            continue
        if x == 9:
            flag = 0
            continue
        if flag == 0:
            l.append(x)
    #print("l =",l)
    return sum(l)


print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))
print(summer_69([]))

