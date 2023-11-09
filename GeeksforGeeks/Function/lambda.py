# s =  "geeksforgeeks"
# (lambda s:print(s))(s)
#
# def power(n):
#     return lambda a : a**n
#
# base = power(2)
# print(base(8))
#
# # lambda functions map() and filter()
# a = [100,2,5,66,78,100]
# filtered = filter(lambda x:x%2==0,a)
# print(list(filtered))
#


n=int(input("Enter the number: "))
c=0
a=1
b=1
if n==0 or n==1:
    print("Yes")
else:
    while c<n:
        c=a+b
        b=a
        a=c
    if c==n:
        print("Yes")
    else:
        print("No")

