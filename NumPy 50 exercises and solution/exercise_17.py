# Exercise 17. How to swap two rows in a 2d numpy array?
import numpy as np

arr=np.arange(9).reshape(3,3)
print(arr)

k=arr[[1,0,2],:]
print(k)