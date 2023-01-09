def foo(a, b):
    return(a + b)


x = foo(2, 3) * 10


#P29 _Liquid volume calculator

from math import pi

def volume(h,r=10):
    liquid_vol = ((4*pi*r**3)/3) -(pi*h**2*(3*r-h)/3)
    return liquid_vol

print(volume(2))


# P30 arguments
# Always put non default parameter first
def foo(a=2, b):
    return a + b