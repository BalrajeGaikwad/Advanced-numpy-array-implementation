"""
Write a NumPy program to create an array of 10's with the same shape and type as the given array.

Sample array: x = np.arange(4, dtype=np.int64)

Expected Output:
[10 10 10 10]
"""

import numpy as np

x=np.ones([1,5])*10

print(x)


a=np.arange(4, dtype=np.int64)
print(a)

b=np.full_like(x,10)
print(b)