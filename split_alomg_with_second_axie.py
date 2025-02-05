"""
Write  a NumPy program that splits an array of shape 4x4 into two arrays along the second axis.

Sample array :
[[ 0 1 2 3]
........
[12 13 14 15]]

Expected Output:
[array([[ 0, 1],
[ 4, 5],
[ 8, 9],
[12, 13]]),

array([[ 2, 3],
[ 6, 7],
[10, 11],
[14, 15]]), array([], shape=(4, 0), dtype=int64)]

""" 

import numpy as np
x=np.arange(16).reshape(4,4)
print("original Array")
print(x)

print("After Splitting this array :-")
print(np.hsplit(x,[2,6]))