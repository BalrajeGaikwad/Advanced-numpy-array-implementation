"""
Write a NumPy program to create a 2-D array whose diagonal equals [4, 5, 6, 8] and 0's elsewhere.

Expected Output:

[[4 0 0 0]
[0 5 0 0]
[0 0 6 0]
[0 0 0 8]]
"""

import numpy as np

x=np.diagflat([4,5,6,8])
print(x)