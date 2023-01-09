# Return keyword
def fun():
    s = 0
    for i in range(10):
        s += i
    return s


print(fun())


# generators
# Yield Keyword
def fun():
    s = 0
    for i in range(10):
        s +=i
        yield s


for i in fun():
    print(i)

