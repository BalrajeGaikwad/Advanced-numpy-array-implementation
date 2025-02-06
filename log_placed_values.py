"""
Write a NumPy program to create a 1-D array of 20 elements spaced evenly on a log scale between 2. and 5., exclusive.

Expected Output:

[ 100. 141.25375446 199.5262315 281.83829313
......................
25118.8643151 35481.33892336 50118.72336273 70794.57843841]
"""
import numpy as np

x=np.logspace(2., 5. , 20, endpoint=False)

print(x)