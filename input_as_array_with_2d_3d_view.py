"""
Write a NumPy program to view inputs as arrays with at least two dimensions, three dimensions.

Expected Output:

View inputs as arrays with at least two dimensions:
[10]
[[ 0. 1.]
[ 2. 3.]]

View inputs as arrays with at least three dimensions:
[[[15]]]
[[[ 0.]
[ 1.]
[ 2.]]]
"""

import numpy as np
x=10

print(np.atleast_1d(x))

x=np.arange(4.0).reshape(2,2)

print(np.atleast_1d(x))

x=15

print(np.atleast_3d(x))

x=np.arange(3.0)

print(np.atleast_3d(x))