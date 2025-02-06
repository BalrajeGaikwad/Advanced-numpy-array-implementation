"""
Write a  NumPy program to create and display every element of a NumPy array.
"""
import numpy as np

x=np.arange(12).reshape(3,4)

for x in np.nditer(x):
    print( x, end=" ")

print()


#Write a  NumPy program to create and display every element of a NumPy array in Fortran order.

# Importing the NumPy library and aliasing it as 'np'
import numpy as np

# Creating a 1-dimensional array 'x' with values from 0 to 11 and reshaping it into a 3x4 array
x = np.arange(12).reshape(3, 4)
print(x)
# Printing a message indicating the elements of the array will be iterated in Fortran order
print("Elements of the array in Fortran array:")

# Using a loop with np.nditer to iterate through each element in the array 'x' in Fortran order
# Printing each element followed by a space and keeping the output in the same line due to the 'end' parameter
for x in np.nditer(x, order="F"):
    print(x, end=' ')

# Printing a newline character to move to the next line after the loop completes
print("\n")