#------------------------------------------------------------------------------------------------#
# flatten():
# flatten() converts a multi-dimensional NumPy Array into a 1D Array.
# 2D → 1D
# 3D → 1D

# The total number of elements remains unchanged.

# Example:
# shape = (2, 3)
# size  = 2 × 3 = 6

# After flatten():
# shape = (6,)
# size  = 6
#------------------------------------------------------------------------------------------------#

#------------------------------------------------------------------------------------------------#
# Structure-1: Flattening a 2D NumPy Array
# <new_array> = <array_name>.flatten()
#------------------------------------------------------------------------------------------------#

# Example
import numpy as np
numbers = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
new_numbers = numbers.flatten()
print(new_numbers)

# Output:
# [10 20 30 40 50 60]


#------------------------------------------------------------------------------------------------#
# Structure-2: Flattening a 3D NumPy Array
# <new_array> = <array_name>.flatten()
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
new_numbers = numbers.flatten()
print(new_numbers)

# Output:
# [10 20 30 40 50 60 70 80]


#------------------------------------------------------------------------------------------------#
# Structure-3: Checking the Shape After Flattening
# <new_array>.shape
#------------------------------------------------------------------------------------------------#

# Example
import numpy as np
numbers = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
new_numbers = numbers.flatten()
print(new_numbers.shape)

# Output:
# (6,)

#------------------------------------------------------------------------------------------------#
# Structure-4: Checking the Dimension After Flattening
# <new_array>.ndim
#------------------------------------------------------------------------------------------------#

# Example
import numpy as np
numbers = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
new_numbers = numbers.flatten()
print(new_numbers.ndim)

# Output:
# 1


#------------------------------------------------------------------------------------------------#
# Structure-5: flatten() Creates a Copy
# <new_array> = <array_name>.flatten()
#------------------------------------------------------------------------------------------------#

# Example
import numpy as np
numbers = np.array([10, 20, 30, 40])
new_numbers = numbers.flatten()
new_numbers[0] = 100
print(numbers)
print(new_numbers)

# Output:
# [10 20 30 40]
# [100  20  30  40]