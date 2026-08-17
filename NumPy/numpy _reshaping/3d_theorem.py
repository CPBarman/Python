#------------------------------------------------------------------------------------------------#
# Structure-1: Reshaping a 3D Array into a 2D Array
# <new_array> = <array_name>.reshape(<rows>, <columns>)
#------------------------------------------------------------------------------------------------#

# Example
import numpy as np
numbers = np.array([
    [
        [10, 20],
        [30, 40]
    ],
    [
        [50, 60],
        [70, 80]
    ]
])
new_numbers = numbers.reshape(4, 2)
print(new_numbers)

# Output:
# [[10 20]
#  [30 40]
#  [50 60]
#  [70 80]]


# Example-2
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
new_numbers = numbers.reshape(3, 4)
print(new_numbers)

# Output:
# [[ 10  20  30  40]
# [ 50  60  70  80]
# [ 90 100 110 120]]


#------------------------------------------------------------------------------------------------#
# Structure-2: Reshaping a 3D Array into a 1D Array
# <new_array> = <array_name>.reshape(<size>)
#------------------------------------------------------------------------------------------------#

# Example
import numpy as np
numbers = np.array([
    [
        [10, 20],
        [30, 40]
    ],
    [
        [50, 60],
        [70, 80]
    ]
])
new_numbers = numbers.reshape(8)
print(new_numbers)

# Output:
# [10 20 30 40 50 60 70 80]


# Example-2
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
new_numbers = numbers.reshape(12)
print(new_numbers)

# Output:
# [ 10  20  30  40  50  60  70  80  90 100 110 120]








#------------------------------------------------------------------------------------------------#
# Rule for reshape()
#------------------------------------------------------------------------------------------------#

# Total Elements = Product of all Dimensions

# For 1D:
# size = n

# For 2D:
# size = rows × columns

# For 3D:
# size = layers × rows × columns

#Example
# Original Array:
# shape = (2, 2, 2)
# size  = 2 × 2 × 2 = 8 #

#Possible:
# (8,)       → 8
# (2, 4)     → 8
# (4, 2)     → 8
# (1, 2, 4)  → 8
# (2, 2, 2)  → 8



# Original Array:
# shape = (2, 2, 3)
# size  = 2 × 2 × 3 = 12 #

# Possible:
# (12,)        → 12
# (1, 12)      → 12
# (2, 6)       → 12
# (3, 4)       → 12
# (4, 3)       → 12
# (6, 2)       → 12
# (12, 1)      → 12

# (1, 2, 6)    → 12
# (1, 3, 4)    → 12
# (1, 4, 3)    → 12
# (1, 6, 2)    → 12
# (2, 1, 6)    → 12
# (2, 2, 3)    → 12
# (2, 3, 2)    → 12
# (2, 6, 1)    → 12
# (3, 1, 4)    → 12
# (3, 2, 2)    → 12
# (3, 4, 1)    → 12
# (4, 1, 3)    → 12
# (4, 3, 1)    → 12
# (6, 1, 2)    → 12
# (6, 2, 1)    → 12
# (12, 1, 1)   → 12
# (1, 12, 1)   → 12
# (1, 1, 12)   → 12