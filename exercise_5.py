# Exercise 5. How to replace items that satisfy a condition with another value in numpy array?
"""
Question: Replace all odd numbers in arr with -1
# input: arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# output: array([ 0, -1,  2, -1,  4, -1,  6, -1,  8, -1])
"""

import numpy as np

arr=np.arange(10)
print(arr)

arr[arr%2==1]=-1
print(arr)