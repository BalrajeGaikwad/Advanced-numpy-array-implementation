"""
Write a NumPy program to change an array's dimension.

Expected Output:

6 rows and 0 columns
(6,)

(3, 3) -> 3 rows and 3 columns
[[1 2 3]
[4 5 6]
[7 8 9]]

Change array shape to (3, 3) -> 3 rows and 3 columns
[[1 2 3]
[4 5 6]
[7 8 9]]
"""

import numpy as np

x=np.array([1,2,3,4,5,6])
print(x.shape)

#creating 2d array

y=np.array([[1,2,3],[4,5,6],[7,8,9]])
print("3 * 3 2d Matrix")
print(y)


#create 1d array with 9 elements 

c=np.array([1,2,3,4,5,6,7,8,9])
c.shape=(3,3)
print(c)