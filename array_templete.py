"""
Write a NumPy program to create an array like the one below.

Expected Output:

[[ 0. 0. 0.]
...........
[ 1. 1. 1.]]
"""

import numpy as np

x=np.tri(4,3,-1)

print(x)