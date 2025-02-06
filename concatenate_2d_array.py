"""
Write a NumPy program to concatenate two 2-dimensional arrays.

Expected Output:

Sample arrays: ([[0, 1, 3], [5, 7, 9]], [[0, 2, 4], [6, 8, 10]]

Expected Output:
[[ 0 1 3 0 2 4]
[ 5 7 9 6 8 10]]
"""
import numpy as np

x=np.array([[0, 1, 3], [5, 7, 9]])

y=np.array([[0, 2, 4], [6, 8, 10]])

c=np.concatenate((x,y),1)

print(c)
k=np.sort(c)
print(k)

print(np.unique(k))


#---------------------------------------------------

a=np.arange(1,11).reshape(2,5)
print("array A",a)

b=np.arange(1,11).reshape(2,5)
print("array B",b)