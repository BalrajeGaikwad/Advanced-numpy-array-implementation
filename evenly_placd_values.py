"""
Write a NumPy program to create a 1-D array of 30 evenly spaced elements between 2.5 and 6.5, inclusive.

Expected Output:

[ 2.5 2.63793103 2.77586207 2.9137931 3.05172414 3.18965517
.................
5.81034483 5.94827586 6.0862069 6.22413793 6.36206897 6.5 ]
"""

import numpy as np

x=np.linspace(2.5, 6.5 , 30)

print(x)