"""
Write a NumPy program to insert a new axis within a 2-D array.

2-D array of shape (3, 4).

Expected Output:

New shape will be will be (3, 1, 4).

Click me to see the sample solution
"""

import numpy as np

x=np.zeros((3,4))
print(x)
y=np.expand_dims(x, axis=1).shape

print(y)