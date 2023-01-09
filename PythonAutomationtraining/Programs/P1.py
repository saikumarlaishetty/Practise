"""
Given:-
-------
data="20-50-36-15-28"

Expected:-
-----------
res="21-51-37-16-29"
"""

data = "20-50-36-15-28"
numlist = data.split("-")
increment = []
for num in numlist:
    increment.append(str(int(num)+1))
print("-".join(increment))

"----------OR--------------"
alst = [str(int(e)+1) for e in data.split("-")]
print("-".join(alst))