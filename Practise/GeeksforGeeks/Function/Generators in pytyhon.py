# Genertor object
def gf():
    yield 1
    yield 2
    yield 3

# x is a generator object
x = gf()

# Iterating over
print(x.__next__())
print(x.__next__())
print(x.__next__())

def gf2():
    yield 1
    yield 2
    yield 3

y = gf2()
for x in y:
    print(x)