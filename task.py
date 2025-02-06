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