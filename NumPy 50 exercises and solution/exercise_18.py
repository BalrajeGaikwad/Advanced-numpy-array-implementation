# Exercise 18. How to reverse the rows of a 2D array?

import numpy as np
arr=np.arange(9).reshape(3,3)
print('original array')
print(arr)

k=arr[::-1,:]
print(k)