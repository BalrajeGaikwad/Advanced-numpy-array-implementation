import numpy as np

# Input 2D NumPy array
input_array = np.array([[2, 4], [5, 6], [7, 9], [8, 10]])

# Step 1: Combine rows to get the desired output
result = []

# First row remains unchanged
result.append(input_array[0])  # Correct

# Second row remains unchanged
result.append(input_array[1])  # Fix: Append without extra brackets

# Third row combines elements from the third and fourth rows
result.append([input_array[2, 0], input_array[3, 1]])  # Merging [7, 10]

# Convert the result to a NumPy array for better representation
result_array = np.array(result)

# Output the result
print(result_array)
