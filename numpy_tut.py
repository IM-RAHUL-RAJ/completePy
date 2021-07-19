import numpy as np
#create arrays in numpy
arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))


print(np.__version__)

# Dimensions in Arrays

arr1 = np.array(42)

print(arr1.ndim)

arr2 = np.array([[1, 2, 3], [4, 5, 6]])

print(arr2)
print(arr2.ndim)


arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr3)
print(arr3.ndim)


arr5 = np.array([1, 2, 3, 4], ndmin=5)

print(arr5)
print('number of dimensions :', arr5.ndim)

# NumPy Array Indexing
#1d
arr6 = np.array([1, 2, 3, 4])

print(arr6[1])
arr6[2]=8   #can change value in numpy array

print(arr6)

#2d
arr7 = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('5th element on 2nd dim: ', arr7[1, 4])

# 3d

arr8 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr8[0, 1, 2])



# Negative Indexing


arr9 = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr9[1, -1])



# Slicing arrays

arr10 = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr10[1:5])

arr11 = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr11[4:])

# Negative Slicing


arr12 = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr12[-3:-1])


# Use the step value to determine the step of the slicing


arr13= np.array([1, 2, 3, 4, 5, 6, 7])

print(arr13[1:5:2])

# Slicing 2-D Arrays
arr14 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr14[1, 1:4])



arr15 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr15[0:2, 1:4])