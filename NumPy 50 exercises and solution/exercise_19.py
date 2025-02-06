# Exercise 19. How to reverse the columns of a 2D array?

import numpy as np

arr=np.arange(9).reshape(3,3)
print('original array')

k=arr[:,::-1]
print(k)