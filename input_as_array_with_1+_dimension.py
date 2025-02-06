"""
Write a NumPy program to convert specified inputs into arrays with at least one dimension.

Expected Output:

[ 12.]
[[ 0. 1. 2.]
[ 3. 4. 5.]]

[array([1]), array([3, 4])]

"""

import numpy as np

x=12.0

print(np.atleast_1d(x))

#create 2 * 3

m=np.arange(6.0).reshape(2,3)
print(m)

print(np.atleast_1d(m))

print(np.atleast_1d(1, [3, 4]))