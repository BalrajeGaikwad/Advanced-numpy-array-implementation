"""
Write a NumPy program to find the union of two arrays. Union will return a unique, sorted array of values in each of the two input arrays.

Array1: [ 0 10 20 40 60 80]
Array2: [10, 30, 40, 50, 70]

Unique sorted array of values that are in either of the two input arrays:
[ 0 10 20 30 40 50 60 70 80]
"""

import numpy as np

array1=np.array([0 ,10 ,20 ,40 ,60 ,80])

array2=np.array([10, 30, 40, 50, 70])

print(np.setxor1d(array1,array2))