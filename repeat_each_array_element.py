"""
Write a NumPy program to repeat array elements.

Expected Output:

[3 3 3 3]
[1 1 2 2 3 3 4 4]
"""

import numpy as np

x=np.repeat(3,4)
print(x)

x=np.array([[1,2],[3,4]])

print(np.repeat(x,2))