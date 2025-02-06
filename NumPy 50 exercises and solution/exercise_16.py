# Exercise 16. How to swap two columns in a 2d numpy array?

import numpy as np
arr=np.arange(9).reshape(3,3)
print("original array")
print(arr)

k=arr[:,[1,0,2]]
print(k)