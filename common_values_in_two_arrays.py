# Write a NumPy program to find common values between two arrays.

import numpy as np

arr=np.array([10,20,30,40,50])
arr1=np.array([40,50])
print(arr , arr1)

print("common")
print(np.intersect1d(arr, arr1))