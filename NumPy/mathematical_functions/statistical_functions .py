#------------------------------------------------------------------------------------------------#
#                              NumPy Statistical Functions

# NumPy provides various statistical functions to perform
# statistical calculations efficiently on NumPy arrays.


#------------------------------------------------------------------------------------------------#
# Structure-1: Sum
#------------------------------------------------------------------------------------------------#
# np.sum(array)
#
# Statement:
# The np.sum() function calculates the sum of all elements
# in the given NumPy array.
#
# Structure:
# np.sum(array)
#------------------------------------------------------------------------------------------------#

#Example
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
result = np.sum(arr)
print(result)

# Output:
# 150


#------------------------------------------------------------------------------------------------#
# Structure-2: Sum of 2D Array
#------------------------------------------------------------------------------------------------#
# np.sum(array)
#
# Statement:
# The np.sum() function can also calculate the sum of all
# elements in a multidimensional NumPy array.
#------------------------------------------------------------------------------------------------#

#Example
import numpy as np
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
result = np.sum(arr)
print(result)

# Output:
# 210


#------------------------------------------------------------------------------------------------#
# Structure-3: Sum Along an Axis
#------------------------------------------------------------------------------------------------#
# np.sum(array, axis=0)
# np.sum(array, axis=1)
#
# Statement:
# The axis parameter specifies the direction along which
# the sum should be calculated.
#
# axis=0 → Sum along columns
# axis=1 → Sum along rows
#------------------------------------------------------------------------------------------------#

#Example
import numpy as np
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
result_column = np.sum(arr, axis=0)
result_row = np.sum(arr, axis=1)
print(result_column)
print(result_row)

# Output:
# [50 70 90]
# [ 60 150]


