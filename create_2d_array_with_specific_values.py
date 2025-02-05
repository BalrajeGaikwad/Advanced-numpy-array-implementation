"""
Write a NumPy program to create an array like the one below.

Expected Output:

[[ 2 3 4]
[ 5 6 7]
[ 0 9 10]
[ 0 0 13]]
"""

import numpy as np

x=np.triu(np.arange(2,14).reshape(4,3),-1)

print(x)