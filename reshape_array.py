"""
Write a NumPy program to create another shape from an array without changing its data.

Reshape 3x2:

[[1 2]
[3 4]
[5 6]]

Reshape 2x3:
[[1 2 3]
[4 5 6]]
"""

import numpy as np

x=np.array([[1,2],[3,4],[5,6]])

print(x)

y=x.reshape(2,3)

print(y)