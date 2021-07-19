# Data Types in Python

# By default Python have these data types:

# strings - used to represent text data, the text is given under quote marks. e.g. "ABCD"
# integer - used to represent integer numbers. e.g. -1, -2, -3
# float - used to represent real numbers. e.g. 1.2, 42.42
# boolean - used to represent True or False.
# complex - used to represent complex numbers. e.g. 1.0 + 2.0j, 1.5 + 2.5j



# Data Types in NumPy



# NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.

# Below is a list of all data types in NumPy and the characters used to represent them.

# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )


import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr.dtype)

arr1 = np.array(['apple', 'banana', 'cherry'])

print(arr1.dtype)


arr = np.array([1, 2, 3, 4], dtype='S')

print(arr)
print(arr.dtype)

# COPY:  //change in only original array

arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42

print(arr)
print(x)


# VIEW //change in both the arrays

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42

print(arr)
print(x)

# Check if Array Owns it's Data
# As mentioned above, copies owns the data, and views does not own the data, but how can we check this?

# Every NumPy array has the attribute base that returns None if the array owns the data.

# Otherwise, the base  attribute refers to the original object.

arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)

# NumPy Array Shape\


arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

print(arr.shape)

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('shape of array :', arr.shape)



# NumPy Array Reshaping
# Reshape From 1-D to 2-D
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(arr)
newarr = arr.reshape(4, 3)

print(newarr)

# Reshape From 1-D to 3-D

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

newarr = arr.reshape(2, 3, 2)

print(newarr)



# Flattening the arrays
# Flattening array means converting a multidimensional array into a 1D array.

# We can use reshape(-1) to do this.

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
newarr = arr.reshape(-1)

print(newarr)