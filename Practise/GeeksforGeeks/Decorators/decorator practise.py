

def new_decorator(my_func):
    def wrap_func():
        print("Code to be executed before wrapper")
        my_func()
        print("Code to be executed after wrapper")
    return wrap_func

def hello():
    print("Hello function to be decorated")


decorated = new_decorator(hello)
print(decorated())

@new_decorator
def another_func():
    print("Another function with decorator @")

print(another_func())
