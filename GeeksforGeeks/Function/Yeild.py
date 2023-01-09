# yeild statement
#  If the body of a def contains
#  yield, the function automatically becomes a
#  generator function.


def Gf():
    yield 1
    yield 2
    yield 3


for v in Gf():
    print(v)