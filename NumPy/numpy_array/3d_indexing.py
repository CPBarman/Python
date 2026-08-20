#================================================================================================#
#                                  3D Array Indexing

# array[layer, row, column]   → Accesses an element using its layer,
#                                row, and column index
#
# Layer indexing starts from 0
# Row indexing starts from 0
# Column indexing starts from 0
#
# First layer  → index 0
# Second layer → index 1
# First row    → index 0
# Second row   → index 1
# First column → index 0
# Second column→ index 1
#================================================================================================#




#------------------------------------------------------------------------------------------------#
# Structure-1: Accessing an Element in a 3D Array
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
