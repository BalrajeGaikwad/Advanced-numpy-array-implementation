"""
Write a NumPy program to sort pairs of a first name and a last name and return their indices (first by last name, then by first name).

first_names = (Betsey, Shelley, Lanell, Genesis, Margery)
last_names = (Battle, Brien, Plotner, Stahl, Woolum)

Expected Output:
[1 3 2 4 0]

"""

# Importing the NumPy library with an alias 'np'
import numpy as np

# Tuple of first names
first_names = ('Margery', 'Betsey', 'Shelley', 'Lanell', 'Genesis')

# Tuple of last names
last_names = ('Woolum', 'Battle', 'Plotner', 'Brien', 'Stahl')

# Lexicographically sorts the tuples of names and returns an array of indices that sorts them
x = np.lexsort((first_names, last_names))

# Displaying the resulting indices that would sort the tuples lexicographically
print(x)
