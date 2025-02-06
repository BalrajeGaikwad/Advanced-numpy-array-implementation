"""
Write a NumPy program to create an array of (3, 4) shapes, multiply every element value by 3 and display the result array.

Expected Output:

Original array elements:
[[ 0 1 2 3]
[ 4 5 6 7]
[ 8 9 10 11]]

New array elements:
[[ 0 3 6 9]
[12 15 18 21]
[24 27 30 33]]
"""
import numpy as np

x=np.arange(12).reshape(3,4)
print(x)

y=x*3
print(y)