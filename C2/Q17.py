# Create, append and remove lists using Numpy
import numpy as np
'''
Use the following methods:

np.array(list) -> create an array

np.append(array, append_iterable) -> append elements of append_iterable to array

np.delete(array, index) -> delete the value at index in array
'''

npArr = np.array([1, 2, 3, 4, 5])
print(npArr)

npArr = np.append(npArr, [6, 7, 8, 9])
print(npArr)

npArr = np.delete(npArr, 1)
print(npArr)