# Write a NumPy program to convert Centigrade degrees into Fahrenheit degrees. Centigrade values are stored in a NumPy array.

"""
c/5 =f-32/9

c=(5(f-32))/9

f= (9c +(32*5))/5
"""

import numpy as np

fvalues=[0, 12, 45.21, 34, 99.91, 32]

f=np.array(fvalues)

print("values in fahhrenheit degree : ")
print(f)

print("values in celsium degree")
print(np.round((5 * f/9-5* 32/9),2))