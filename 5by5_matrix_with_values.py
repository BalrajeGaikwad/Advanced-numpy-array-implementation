"""
Write a NumPy program to create a 5x5 matrix with row values ranging from 0 to 4.

Original array:
[[ 0. 0. 0. 0. 0.]
.........
[ 0. 0. 0. 0. 0.]]

Row values ranging from 0 to 4.
[[ 0. 1. 2. 3. 4.]
..........
[ 0. 1. 2. 3. 4.]]
"""

import numpy as np

a=np.zeros((5,5))

print("original array")
print(a)

a=a+np.arange(5)

print("Arrayb after adding the new elements")
print(a)