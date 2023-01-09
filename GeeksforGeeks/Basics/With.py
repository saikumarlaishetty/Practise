# Using with statement
with open('file_path','w') as file:
    file.write("Hello world!")

# as keyword
import math as gfg
print(gfg.factorial(5))

# Pass keyword
n = 10
for i in range(n):
    # Pass can be used as placeholder when code is to added later
    pass

# Lambda
g = lambda x: x*x*x
print(g(7))