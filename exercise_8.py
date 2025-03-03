#Exercise 8. How to stack two arrays vertically?

"""
Question: Stack arrays a and b vertically
# input: a = np.arange(10).reshape(2,-1)
#        b = np.repeat(1, 10).reshape(2,-1)

# output: array([[0, 1, 2, 3, 4],
#                [5, 6, 7, 8, 9],
#                [1, 1, 1, 1, 1],
#                [1, 1, 1, 1, 1]])

"""
import numpy as np

a=np.arange(10).reshape(2,-1)
print(a)
b=np.repeat(1,10).reshape(2,-1)
print(b)

k=np.vstack([a,b])    
print(k)