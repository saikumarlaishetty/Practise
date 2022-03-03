# Demonstrate pure functions

def pure_func(List):
    New_List = []
    for i in List:
        New_List.append(i**2)

    return New_List

Original_List = [1,2,3,4]
Modified_List = pure_func(Original_List)

print("Original List :",Original_List)
print("Modified LIst :",Modified_List)

# Recursion

def Sum(L,i,n,count):

    # Base case
    if n <= i:
        return count

    count += L[i]

    # Going into the recursion
    count = Sum(L,i+1,n,count)
    return count

L = [1,2,3,4,5]
count = 0
n =len(L)
print(Sum(L,0,n,count))

