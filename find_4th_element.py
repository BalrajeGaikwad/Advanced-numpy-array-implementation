"""
Write a NumPy program to find the 4th element of a specified array.

Expected Output:

[[ 2 4 6]
[ 6 8 10]]

Forth e1ement of the array:
6
"""

import numpy as np

x=np.array([[2,4,6],[6,8,10]])

print(x)

print(x[1][0])

e=x.flat[3]
print(e)