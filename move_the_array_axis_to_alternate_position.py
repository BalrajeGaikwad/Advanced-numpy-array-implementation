"""
Write a NumPy program to move array axes to alternate positions. Other axes remain in their original order.

Expected Output:

(3, 4, 2)
(4, 2, 3)
"""
import numpy as np
x=np.zeros((2,3,4))

print(np.moveaxis(x, 0, -1).shape)

print(np.moveaxis(x,-1,0).shape)