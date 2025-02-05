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