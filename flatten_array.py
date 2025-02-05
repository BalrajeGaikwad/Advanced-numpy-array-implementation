"""
Write a NumPy program to create a contiguous flattened array.

Original array:

[[10 20 30]
[20 40 50]]

New flattened array:
[10 20 30 20 40 50]
"""

import numpy as np

x=np.array([[1,2,3],[4,5,6]])
print(x)

y=np.ravel(x)
print(y)