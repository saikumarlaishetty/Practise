def h(func):
    def inner(*args, **kwargs):
        return_value = func(*args,**kwargs)
        print("after execution")
        return return_value
    return inner

@h
def sum_of_two_numbers(a,b):
    print("Inside the function")
    return a+b

#sum_of_two_numbers = h(sum_of_two_numbers(a,b))
a,b = 1,2
print("Sum = ", sum_of_two_numbers(a,b))