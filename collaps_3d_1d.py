"""
Write a NumPy program to collapse a 3-D array into a one-dimensional array.

Expected Output:

3-D array:
[[ 1. 0. 0.]
[ 0. 1. 0.]
[ 0. 0. 1.]]

One dimension array:
[ 1. 0. 0. 0. 1. 0. 0. 0. 1.]
"""

import numpy as np

x=np.array([[1,0,0],[0,1,0],[0,0,1]])

print(x)

print(x.reshape(9,))


#-------------------------------------------

x=np.eye(3)

f=np.ravel(x, order='F')

print("one dimension array ")
print(f)