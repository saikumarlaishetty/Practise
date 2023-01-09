class C(object):
    def __init__(self):
        self.c = 21

        # d is private instance variable
        self.__d = 42


class D(C):
    def __init__(self):
        self.e = 84
        C.__init__(self)


object1 = D()
# print(object1.d)  Produces an error as d

