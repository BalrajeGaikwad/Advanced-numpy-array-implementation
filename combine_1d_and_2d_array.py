"""
Write a NumPy program to combine a one and two dimensional array together and display their elements.

Expected Output:

One dimensional array:
[0 1 2 3]

Two dimensional array:
[[0 1 2 3]
[4 5 6 7]]
0:0
1:1
2:2
3:3
0:4
1:5
2:6
3:7
"""

import numpy as np

x=np.arange(4)
print(x)

y=np.arange(8).reshape(2,4)
print(y)

for a, b in np.nditer([x, y]):
    print("%d:%d" % (a, b), end=' ')  # Printing pairs of elements from 'x' and 'y' together

# Printing a newline character to separate the output
print() 