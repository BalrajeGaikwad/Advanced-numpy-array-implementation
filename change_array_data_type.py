"""
Write a NumPy program to change an array's data type.

Expected Output:

[[ 2 4 6]
[ 6 8 10]]

Data type of the array x is: int32

New Type: float64
[[ 2. 4. 6.]
[ 6. 8. 10.]]
"""
import numpy as np

x=np.array([[1,2,3],[4,5,6]], np.int32)

print(x)

print(x.dtype)

y=x.astype(float)
print(y.dtype)