"""
Write a NumPy program (using numpy) to sum all the multiples of 3 or 5 below 100.

Expected Output:
[ 3 5 6 9 10 12 15 18 20 21 24 25 27 30 33 35 36 39 40 42 45 48 50 51 54
55 57 60 63 65 66 69 70 72 75 78 80 81 84 85 87 90 93 95 96 99]
2318
"""


import numpy as np

x=np.arange(100)
print(x)

n=x[(x%3==0) | (x%5==0)]

print(n)