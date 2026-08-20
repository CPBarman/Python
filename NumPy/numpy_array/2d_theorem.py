#================================================================================================#
#                                    2D NumPy Array 

# np.ndim   → Returns the number of dimensions of an array
# np.size   → Returns the total number of elements in an array
# np.shape  → Returns the dimensions of an array
# np.dtype  → Returns the data type of array elements
#================================================================================================#




#------------------------------------------------------------------------------------------------#
# Structure-1: Creating a Two-Dimensional (2D) Array
# <array_name> = np.array([
#     [value1, value2, value3],
#     [value4, value5, value6]
# ])
#------------------------------------------------------------------------------------------------#

# Example-1
import numpy as np
numbers = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(numbers)

# Output:
# [[10 20 30]
# [40 50 60]]


#------------------------------------------------------------------------------------------------#
# Structure-2: Finding the Number of Dimensions Using ndim
# <array_name>.ndim
# ndim  = Number of Dimensions
# shape = Size of Each Dimension (Number of Rows & Columns)
# size  = Total Number of Elements
#------------------------------------------------------------------------------------------------#

#Example-1
import numpy as np
numbers = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(numbers.ndim)
print(numbers.shape)
print(numbers.size)

# Output:
# 2
# (2, 3)
# 6