"""
Write a NumPy program to convert 1-D arrays as columns into a 2-D array.
Sample array: (10,20,30), (40,50,60)
"""

import numpy as np

a=np.array((10,20,30))
b=np.array((40,50,60))

c=np.column_stack((a,b))

print(c)