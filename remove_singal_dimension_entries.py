"""
Write a NumPy program to remove single-dimensional entries from a specified shape.

Specified shape: (3, 1, 4)

Expected Output: (3, 4)

Click me to see the sample solution

"""

import numpy as np

x=np.ones((3,1,4))
## Squeezing the array x to remove single-dimensional entries, 
# resulting in an array with shape (3, 4), and printing its shape

print(np.squeeze(x).shape)