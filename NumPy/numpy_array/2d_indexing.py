#================================================================================================#
#                                  2D Array Indexing

# array[row, column]   → Accesses an element using its row and column index
#
# Row indexing starts from 0
# Column indexing starts from 0
#
# First row    → index 0
# Second row   → index 1
# First column → index 0
# Second column→ index 1
#================================================================================================#




#------------------------------------------------------------------------------------------------#
# Structure-1: Accessing an Element in a 2D Array
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
# Structure-2: Accessing a Column from a 2D Array
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


