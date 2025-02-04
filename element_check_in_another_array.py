# Write a NumPy program to test whether each element of a 1-D array is also present in a second array.

import numpy as np
arr=np.array([0,10,20,30,40,50])
print(arr)

arr2=np.array([0,40])                               #np.in1d
print(arr2)

print("Compare Each element of 'array1 and array2")
print(np.in1d(arr,arr2))