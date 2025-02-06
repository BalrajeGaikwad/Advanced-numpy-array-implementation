"""
Write a NumPy program to get the number of non-zero elements in an array.

Expected Output:

Original array:
[[ 0 10 20]
[20 30 40]]

Number of non zero elements in the above array:
5
"""

import numpy as np

arr=np.array([[1,2,3],[4,5,6],[0,6,8]])

print("original array")
print(arr)

num=np.count_nonzero(arr)
print(num)

for i in len(num):
    print(i(num))