"""
Write a NumPy program to test whether specified values are present in an array.

Expected Output:

Original array:
[[ 1.12 2. 3.45]
[ 2.33 5.12 6. ]]

True
False
True
False
True
"""

import numpy as np

x = np.array([[1.12, 2.0, 3.45], [2.33, 5.12, 6.0]], float)
print("original array")

print(1.12 in x)
print(2.0 in x)
print(3.45 in x)
print(1.12 in x)
print(5.12 in x)
print(1.12 in x)
print(1.12 in x)