"""
Write a NumPy program to move the specified axis backwards, until it lies in a given position.

Move the following 3rd array axes to first position.
(2,3,4,5)

Sample Expected Output:
(2, 5, 3, 4)

"""

import numpy as np

x=np.ones((2,3,4,5))

print(np.rollaxis(x, 3,1).shape)