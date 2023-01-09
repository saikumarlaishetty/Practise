"""
Write a function that checks whether a number is in a given range (inclusive of high and low)


def ran_check(num,low,high):
    #Check if num is between low and high (including low and high)
    if num in range(low,high+1):
        print('{} is in the range between {} and {}'.format(num,low,high))
    else:
        print('The number is outside the range.')

"""

def ran_check(num,low,high):
    if low <= num <= high :
        print("{0} is between {1} and {2}".format(num,low,high))


# Check
ran_check(5,2,7)