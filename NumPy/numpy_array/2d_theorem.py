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
# Structure-2: Accessing an Element in a 2D Array
# <array_name>[<row_index>, <column_index>]
#------------------------------------------------------------------------------------------------#

# Example
import numpy as np
numbers = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(numbers[0, 1])
print(numbers[1, 2])

# Output:
# 20
# 60


#------------------------------------------------------------------------------------------------#
# Structure-3: Accessing a Column from a 2D Array
# <array_name>[:, <column_index>]
#------------------------------------------------------------------------------------------------#

# Example
import numpy as np
numbers = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(numbers[:, 1])

# Output:
# [20 50]


#------------------------------------------------------------------------------------------------#
# Structure-4: Finding the Number of Dimensions Using ndim
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