#================================================================================================#
#                                    3D NumPy Array 

# np.ndim   → Returns the number of dimensions of an array
# np.size   → Returns the total number of elements in an array
# np.shape  → Returns the dimensions of an array
# np.dtype  → Returns the data type of array elements
#================================================================================================#




#------------------------------------------------------------------------------------------------#
# Structure-1: Creating a Three-Dimensional (3D) Array
# <array_name> = np.array([
#     [
#         [value1, value2, value3],
#         [value4, value5, value6]
#     ],
#     [
#         [value7, value8, value9],
#         [value10, value11, value12]
#     ]
# ])
#------------------------------------------------------------------------------------------------#

# Example
import numpy as np

numbers = np.array([
    [
        [10, 20, 30],
        [40, 50, 60]
    ],
    [
        [70, 80, 90],
        [100, 110, 120]
    ]
])
print(numbers)

#Output:
# [[[ 10  20  30]
#  [ 40  50  60]]

# [[ 70  80  90]
# [100 110 120]]]


#------------------------------------------------------------------------------------------------#
# Structure-2: Finding the Number of Dimensions
# <array_name>.ndim
# ndim  = Number of Dimensions
# shape = Size of Each Dimension (Number of Rows & Columns)
# size  = Total Number of Elements
#------------------------------------------------------------------------------------------------#

# Example
import numpy as np
numbers = np.array([
    [
        [10, 20, 30],
        [40, 50, 60]
    ],
    [
        [70, 80, 90],
        [100, 110, 120]
    ]
])
print(numbers.ndim)
print(numbers.shape)
print(numbers.size)

# Output:
# 3
# (2, 2, 3)
# 12

