"""
Syntax: map(fun, iter)

Parameters:
fun: It is a function to which map passes each element of given iterable.
iter: It is a iterable which is to be mapped.

Return Type: Returns an iterator of map class.
"""

def addition(n):
    return n + n


numbers = (1, 2, 3, 4)
results = map(addition, numbers)

print(results)

for result in results:
    print(result)


def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if variable in letters:
        return True
    else:
        return False


sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
filtered = filter(fun,sequence)
print("The filtered letters are :")
for s in filtered:
    print(s)

