# Write a NumPy program to convert a list and tuple into arrays.

import numpy as np

l=[1,2,3,4]
print(l)

s=([4,5,6,7],[9,7,6,5])

print(s)

print(np.asarray(l))
print(np.asarray(s))