# Exercise 4. How to extract items that satisfy a given condition from 1D array?

import numpy as np

arr=np.arange(10)

k=arr[arr%2==0]

print(k)