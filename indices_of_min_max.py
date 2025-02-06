"""
Write a NumPy program to find the indices of the maximum and minimum values along the given axis of an array.

Original array: [1 2 3 4 5 6]

Maximum Values: 5
Minimum Values: 0
"""

import numpy as np
x=np.array([[1,2,3,4,5,6,7]])
print(x)

print("max value index",np.argmax(x))

print("max value index",np.argmin(x))