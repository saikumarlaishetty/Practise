def decor1(func):
    def inner():
        x = func()
        print("Inner decor1 ***")
        return x*x
    print("decor1")
    return inner

def decor(func):
    def inner():
        x = func()
        print("Inner decor !!!")
        return 2*x
    print("decor")
    return inner

@decor1
@decor
def num():
    return 10

print(num())

# The above example is similar to calling the function as –
#
# decor1(decor(num))