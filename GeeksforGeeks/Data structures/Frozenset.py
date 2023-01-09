"""
Frozen sets in Python are immutable objects that
only support methods and operators that produce a
result without affecting the frozen set or sets to
which they are applied. While elements of a set can
be modified at any time,
 elements of the frozen set remain the same after creation.
"""

String ="GeeksForGeeks"
set1 = set(String)
print(set1)

Fset1 = frozenset(String)
print(Fset1)

