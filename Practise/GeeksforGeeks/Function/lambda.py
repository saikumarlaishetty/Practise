s =  "geeksforgeeks"
(lambda s:print(s))(s)

def power(n):
    return lambda a : a**n

base = power(2)
print(base(8))

# lambda functions map() and filter()
a = [100,2,5,66,78,100]
filtered = filter(lambda x:x%2==0,a)
print(list(filtered))

