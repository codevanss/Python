# Create a 4X2 integer array and Prints its attributes
# import numpy

# firstArray = numpy.empty([4,2], dtype = numpy.uint16) 
# print("Printing Array")
# print(firstArray)

# print("Printing numpy array Attributes")
# print("1> Array Shape is: ", firstArray.shape)
# print("2>. Array dimensions are ", firstArray.ndim)
# print("3>. Length of each element of array in bytes is ", firstArray.itemsize)

# Create a 5X2 integer array from a range between 100 to 200 such that the difference between each element is 10
# import numpy

# print("Creating 5X2 array using numpy.arange")
# sampleArray = numpy.arange(100, 200, 10)
# sampleArray = sampleArray.reshape(5,2)
# print (sampleArray)

# Following is the provided numPy array. Return array of items by taking the third column from all rows
# import numpy

# sampleArray = numpy.array([[11 ,22, 33], [44, 55, 66], [77, 88, 99]]) 
# print("Printing Input Array")
# print(sampleArray)

# print("\n Printing array of items in the third column from all rows")
# newArray = sampleArray[...,2]
# print(newArray)

# Return array of odd rows and even columns from below numpy array
# import numpy

# sampleArray = numpy.array([[3 ,6, 9, 12], [15 ,18, 21, 24], 
# [27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]]) 
# print("Printing Input Array")
# print(sampleArray)

# print("\n Printing array of odd rows and even columns")
# newArray = sampleArray[::2, 1::2]
# print(newArray)

# Create a result array by adding the following two NumPy arrays. Next, modify the result array by calculating the square of each element
# import numpy

# arrayOne = numpy.array([[5, 6, 9], [21 ,18, 27]])
# arrayTwo = numpy.array([[15 ,33, 24], [4 ,7, 1]])

# resultArray  = arrayOne + arrayTwo
# print("addition of two arrays is \n")
# print(resultArray)

# for num in numpy.nditer(resultArray, op_flags = ['readwrite']):
#    num[...] = num*num
# print("\nResult array after calculating the square root of all elements\n")
# print(resultArray)

# Split the array into four equal-sized sub-arrays
# import numpy

# print("Creating 8X3 array using numpy.arange")
# sampleArray = numpy.arange(10, 34, 1)
# sampleArray = sampleArray.reshape(8,3)
# print (sampleArray)

# print("\nDividing 8X3 array into 4 sub array\n")
# subArrays = numpy.split(sampleArray, 4) 
# print(subArrays)

# Sort following NumPy array
# import numpy

# print("Printing Original array")
# sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]]) 
# print (sampleArray)

# sortArrayByRow = sampleArray[:,sampleArray[1,:].argsort()]
# print("Sorting Original array by secoond row")
# print(sortArrayByRow)

# print("Sorting Original array by secoond column")
# sortArrayByColumn = sampleArray[sampleArray[:,1].argsort()]
# print(sortArrayByColumn)

#  Print max from axis 0 and min from axis 1 from the following 2-D array.
# import numpy

# print("Printing Original array")
# sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]]) 
# print (sampleArray)

# minOfAxisOne = numpy.amin(sampleArray, 1) 
# print("Printing amin Of Axis 1")
# print(minOfAxisOne)

# maxOfAxisOne = numpy.amax(sampleArray, 0) 
# print("Printing amax Of Axis 0")
# print(maxOfAxisOne)

#  Delete the second column from a given array and insert the following new column in its place.
# import numpy

# print("Printing Original array")
# sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]]) 
# print (sampleArray)

# print("Array after deleting column 2 on axis 1")
# sampleArray = numpy.delete(sampleArray , 1, axis = 1) 
# print (sampleArray)

# arr = numpy.array([[10,10,10]])

# print("Array after inserting column 2 on axis 1")
# sampleArray = numpy.insert(sampleArray , 1, arr, axis = 1) 
# print (sampleArray)

# Create two 2-D arrays and Plot them using matplotlib
import numpy as np
import matplotlib.pyplot as plt

# Create two 2D NumPy arrays
array1 = np.random.randint(1, 100, (5, 5))  # 5x5 matrix with random values (1-100)
array2 = np.random.randint(1, 100, (5, 5))  # Another 5x5 matrix

# Plotting the first array
plt.subplot(1, 2, 1)  # 1 row, 2 columns, position 1
plt.imshow(array1, cmap='coolwarm', interpolation='nearest')
plt.colorbar()  # Add color scale
plt.title("Array 1 Heatmap")

# Plotting the second array
plt.subplot(1, 2, 2)  # 1 row, 2 columns, position 2
plt.imshow(array2, cmap='coolwarm', interpolation='nearest')
plt.colorbar()  # Add color scale
plt.title("Array 2 Heatmap")

# Show the plots
plt.tight_layout()
plt.show()
