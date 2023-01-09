"""
Write a Python function to multiply all the numbers in a list.

Sample List : [1, 2, 3, -4]
Expected Output : -24

"""

def multiply(numbers):
    temp = 1
    for x in numbers:
        temp *= x

    print(temp)
multiply([1,2,3,-4])
