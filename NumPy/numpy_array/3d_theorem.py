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

#------------------------------------------------------------------------------------------------#
# Structure-3: Accessing an Element in a 3D Array
# <array_name>[<layer_index>, <row_index>, <column_index>]
#------------------------------------------------------------------------------------------------#

#Example-1
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
print(numbers[0, 1, 2])
print(numbers[1, 0, 1])

# Output:
# 60
# 80


#Example-2
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
print(numbers[0, 1, 2])
print(numbers[1, 0, 1])

# Output:
# 60
# 80
