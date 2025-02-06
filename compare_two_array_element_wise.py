"""
Write a NumPy program to compare two arrays using NumPy.

Array a: [1 2]
Array b: [4 5]

a > b
[False False]

a >= b
[False False]

a < b
[ True True]

a <= b
[ True True ]
"""

import numpy as np

a = np.array([1, 2])
b = np.array([4, 5])

print("a > b")
print(np.greater(a,b))

print("a >= b")
print(np.greater_equal(a,b))

print("a < b")
print(np.less(a,b))

print("a<= b")
print(np.less_equal(a,b))