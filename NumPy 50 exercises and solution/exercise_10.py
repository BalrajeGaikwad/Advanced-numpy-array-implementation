#Exercise 10. How to generate custom sequences in numpy without hardcoding?¶
"""
# Input: a = np.array([1,2,3])
# Output: array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])
"""

import numpy as np
a=np.array([1,2,3])
b=np.hstack((np.repeat(a,3),np.tile(a,3)))
#np.hstack((np.repeat(a, 3), np.tile(a, 3)))
print(b)