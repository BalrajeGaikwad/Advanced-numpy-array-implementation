"""
Write a NumPy program to create a 1-D array with values from 0 to 50 and an array from 10 to 50.

Expected Output:

Array from 0 to 50:

[ 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49]

Array from 10 to 50:
[10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34
35 36 37 38 39 40 41 42 43 44 45 46 47 48 49]
"""

import numpy as np

x=np.arange(0,51)
print(x)

y=np.arange(10,50)
print(y)