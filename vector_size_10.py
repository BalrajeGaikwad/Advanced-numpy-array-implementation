"""
Write a NumPy program to create a vector of size 10 with values ranging from 0 to 1, both excluded.

Expected Output:

[ 0.09090909 0.18181818 0.27272727 0.36363636 0.45454545 0.54545455
0.63636364 0.72727273 0.81818182 0.90909091]
"""

import numpy as np

x=np.linspace(0,1,12, endpoint= True)[1:-1]
print(x)