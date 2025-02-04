# Write a NumPy program to find the set difference between two arrays. The set difference will return sorted, distinct values in array1 that are not in array2.

"""
Expected Output:

Array1: [ 0 10 20 40 60 80]
Array2: [10, 30, 40, 50, 70, 90]

Set difference between two arrays:
[ 0 20 60 80]

"""

import numpy as np

a=np.array([0,10,20,30,40,50,60])
b=np.array([40,50,60,10])

print(np.setdiff1d(a,b))