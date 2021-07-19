# NumPy Array Iterating


import numpy as np

arr = np.array([1, 2, 3])

for x in arr:
  print(x)


#   Iterating 2-D Arrays

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
  print(x)

#   Iterating 3-D Arrays

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  print(x)
  


arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
  for y in x:
    for z in y:
      print(z)



# Iterating Arrays Using nditer()
# The function nditer() is a helping function that can be used from very basic to very advanced iterations. It solves some basic issues which we face in iteration, lets go through it with examples.

# Iterating on Each Scalar Element

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
  print(x)


# Joining NumPy Arrays


arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)



# Join two 2-D arrays along rows (axis=1):



arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.concatenate((arr1, arr2), axis=1)

print(arr)


# NumPy Splitting Array

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)
arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 4)

print(newarr)



# NumPy Searching Arrays


arr = np.array([1, 2, 3, 4, 5, 4, 4])
# Find the indexes where the value is 4:
x = np.where(arr == 4)

print(x)

# Find the indexes where the values are even:

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0)

print(x)

# Search Sorted


# Find the indexes where the value 7 should be inserted:


arr = np.array([6, 7, 8, 9])

x = np.searchsorted(arr, 7)

print(x)


# NumPy Sorting Arrays

arr = np.array([3, 2, 0, 1])

print(np.sort(arr))

arr = np.array(['banana', 'cherry', 'apple'])

print(np.sort(arr))

arr = np.array([True, False, True])

print(np.sort(arr))


# Sorting a 2-D Array
# If you use the sort() method on a 2-D array, both arrays will be sorted:


arr = np.array([[3, 2, 4], [5, 0, 1]])

print(np.sort(arr))



# Random Numbers in NumPy
from numpy import random
x2 = random.randint(100)

print(x2)

# Generate Random Float
# The random module's rand() method returns a random float between 0 and 1.
# Generate a random float from 0 to 1:

from numpy import random

x1 = random.rand()
print(x1)

# Generate Random Array
x=random.randint(100, size=(5))

print(x)

print(x)