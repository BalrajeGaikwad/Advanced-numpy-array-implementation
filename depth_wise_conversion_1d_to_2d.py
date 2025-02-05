"""
Write a NumPy program to convert (in sequence depth wise (along the third axis)) two 1-D arrays into a 2-D array.

Sample array: (10,20,30), (40,50,60)

Expected Output:

[[[10 40]]
[[20 50]]
[[30 60]]]
"""

import numpy as np

# Creating NumPy arrays 'a' and 'b' with vertical shapes
a = np.array([[10], [20], [30]])
b = np.array([[40], [50], [60]])

# Stacking arrays 'a' and 'b' along the third axis using np.dstack
c = np.dstack((a, b))

# Printing the resulting array 'c'
print(c)