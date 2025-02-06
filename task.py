<<<<<<< HEAD
import numpy as np

x=np.array([[1,2]])
y=np.array([[3,5]])
z=np.array([[4,7]])
p=np.array([[8,10]])

x=np.concatenate((x,y,z,p))
print(x)

"""input=np.array([
    [x[0,0],x[0,1]],
    [x[1,0],x[1,1]],
    [x[2,0],x[2,1]],
    [x[3,0],x[3,1]]
 
])
"""
# Step 1: Combine adjacent rows
result = []

for i in range(0, len(x), 2):
    if i + 1 < len(x):
        # Merge the arrays at index i and i+1
        merged_array = [x[i, 0], x[i+1, 1]]
        result.append(merged_array)
    else:
        # Add the last array as it is
        result.append(x[i])

# Convert the result to a NumPy array for better representation
result_array = np.array(result)

# Output the result
print(result_array)
=======
"""import numpy as np

a=np.arange(1,11).reshape(5,2)
print("array of a")
print(a)

b=np.arange(1,11).reshape(5,2)
print("array of b")
print(b)

first_array=([[]])

first_array = np.array([
    [a[0, 0], a[0, 1]],  
    [a[1, 0], a[1, 1]], 
    [a[2, 0], a[3, 0]],
    [a[3, 1], a[4, 0]],
    [a[3, 1], a[4, 0]]   
])
print("first array")
print(first_array)
second_array = np.array([
    [b[0, 1], b[1, 0]],  
    [b[1, 1], b[2, 0]],  
    [b[2, 1], b[3, 0]],  
    [b[3, 1], b[4, 0]],
    [b[3, 1], b[4, 0]]   
])
print("second array")
print(second_array)

result = np.vstack((first_array, second_array)) 

print("result")
print(result)

unique=np.sort(result)
print(unique)"""

import numpy as np


a=np.arange(1,11).reshape(5,2)
print("array A",a)

b=np.arange(1,11).reshape(5,2)
print("array B",b)

first_array = np.array([
    [a[0, 0], a[0, 1]],  
    [a[1, 0], a[1, 1]], 
    [a[2, 0], a[3, 0]],
    [a[3, 1], a[4, 0]],
    [a[3, 1], a[4, 0]]   
])
print("first array")
print(first_array)
second_array = np.array([
    [b[0, 1], b[1, 0]],  
    [b[1, 1], b[2, 0]],  
    [b[2, 1], b[3, 0]],  
    [b[3, 1], b[4, 0]],
    [b[3, 1], b[4, 0]]   
])
print("second array")
print(second_array)

c=np.concatenate((first_array,second_array),0)

print(c)
k=np.sort(c)
print("sorted array")
print(k)

p=np.sort(c, axis=0)
print("sorted feom p")
print(p)
print(np.unique(k))
>>>>>>> bf925011e58cd7ac1c1f1d77801d1ca633996d2e
