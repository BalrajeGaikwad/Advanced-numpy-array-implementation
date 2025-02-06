#Exercise 3. How to create a boolean array?¶

import numpy as np

a=np.full((3,3), True, dtype=bool)
#or

b=np.ones((3,3), dtype=bool)

c=np.ones((9), dtype=bool).reshape(3,3)

print(a,b,c)