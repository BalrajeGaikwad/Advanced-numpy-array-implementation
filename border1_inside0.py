# Write a NumPy program to create a 2D array with 1 on the border and 0 inside.

import numpy as np

x=np.ones((5,5))
print(x)

x[1:-1, 1:-1]=0

print(x)