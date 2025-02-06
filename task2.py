import numpy as np

video_array = np.array([[1, 2], [3, 5], [4, 7], [8, 10]])

result = []
result.append(video_array[0])
result.append([video_array[1, 0], video_array[2, 1]])
result.append(video_array[3])
result_array = np.array(result)
print("result_array",result_array)

audio = np.array([[2, 4], [5, 6], [7, 9], [8, 10]])
audio_result = []
audio_result.append(audio[0])  
audio_result.append(audio[1])  
audio_result.append([audio[2, 0], audio[3, 1]])  
audio_result_array = np.array(audio_result)
print("audio_result_array",audio_result_array)


merged_array = np.vstack((result_array, audio_result_array))

# Sort by the first column, then by the second column
sorted_array = merged_array[np.lexsort((merged_array[:, 1], merged_array[:, 0]))]

# Convert to a list of lists
output = sorted_array.tolist()

# Print the output
print(output)
