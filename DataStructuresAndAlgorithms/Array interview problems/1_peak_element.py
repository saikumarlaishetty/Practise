# https://www.geeksforgeeks.org/find-a-peak-in-a-given-array/

# 1st method
def findPeak(arr,n):
    peak = max(arr)
    return arr.index(peak)


# 2nd method
def findPeak(arr,n):



# Driver code.
arr = [ 1, 3, 20, 4, 1, 0 ]
n = len(arr)
print("Index of a peak point is", findPeak(arr, n))