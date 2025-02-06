"""
Write a NumPy program to change two array axes.

Sample array: [[1 2 3]]

Expected Output:
[[1]
[2]
[3]]
"""

import numpy as np

x=np.array([[1,2,3]])

# Swapping the axes (dimensions) of the array using 'swapaxes' method
# Swapping axis 0 (rows) with axis 1 (columns)

y=np.swapaxes(x,0,1)
print(y)