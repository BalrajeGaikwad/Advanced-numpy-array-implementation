"""
Write a NumPy program to create a 5x5x5 cube of 1's.

Expected Output:

[[[1 1 1 1 1]
[1 1 1 1 1]
[1 1 1 1 1]
[1 1 1 1 1]
[1 1 1 1 1]]
............
[[1 1 1 1 1]
[1 1 1 1 1]
[1 1 1 1 1]
[1 1 1 1 1]
[1 1 1 1 1]]]
"""

import numpy as np

x=np.zeros((5,5,5)).astype(int)+1
print(x)
