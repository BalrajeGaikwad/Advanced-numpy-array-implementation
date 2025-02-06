# Exercise 6. How to replace items that satisfy a condition without affecting the original array?
"""
# input: arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# output: out
# array([ 0, -1,  2, -1,  4, -1,  6, -1,  8, -1])
# arr
# array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
"""

import numpy as np

arr=np.arange(10)
print(arr)

k=arr.copy()

k[k%2==1]=-1
print(k)