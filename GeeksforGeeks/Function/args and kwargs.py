#Using the *, the variable that we associate
#with the * becomes an iterable meaning you can do
# things like iterate over
# it, run some higher-order functions such as map and filter, etc.

def myfunc(*arg):
    for ar in arg:
        print(ar)

myfunc('Hello','do','your','work')


# first extra argument

def myfunc(args,*arg):
    print("first",args)
    for ar in arg:
        print(ar)

myfunc('Hello','do','your','work')

# Keyword arguments
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


# Driver code
myFun(first='Geeks', mid='for', last='Geeks')


# Keyword arguments with one extra argument

def myFun(f,**kwargs):
    print("First",f)
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))


# Driver code
myFun(" U",first='Geeks', mid='for', last='Geeks')


# Using args and Kwargs

def fu(arg1,arg2,arg3):
    print(arg1)
    print(arg2)
    print(arg3)

args = ("geeks","for","geeks")
fu(*args)

kwargs = {"arg1":"Geeks","arg2":"for","arg3":"Geeks"}
fu(*kwargs)

# args and kwargs in same line of function
def ar(*ars,**kwargs):
    print(*ars)
    print(**kwargs)

ar('geeks','for','geeks',first="Geeks",mid="for",last="Geeks")

