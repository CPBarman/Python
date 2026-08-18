#------------------------------------------------------------------------------------------------#
# Structure-1: Using ravel() on a 2D NumPy Array
# <new_array> = <array_name>.ravel()
#------------------------------------------------------------------------------------------------#

# Example
import numpy as np
numbers = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
new_numbers = numbers.ravel()
print(new_numbers)

# Output:
# [10 20 30 40 50 60]

#------------------------------------------------------------------------------------------------#
# Structure-2: Using ravel() on a 3D NumPy Array
# <new_array> = <array_name>.ravel()
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
new_numbers = numbers.ravel()
print(new_numbers)

# Output:
# [10 20 30 40 50 60 70 80]

#------------------------------------------------------------------------------------------------#
# Structure-3: Checking the Shape After ravel()
# <new_array>.shape
#------------------------------------------------------------------------------------------------#

# Example
import numpy as np
numbers = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
new_numbers = numbers.ravel()
print(new_numbers.shape)

# Output:
# (6,)

#------------------------------------------------------------------------------------------------#
# Structure-4: ravel() Creates a View When Possible
# <new_array> = <array_name>.ravel()
#------------------------------------------------------------------------------------------------#

# Example
import numpy as np
numbers = np.array([10, 20, 30, 40])
new_numbers = numbers.ravel()
new_numbers[0] = 100
print(numbers)
print(new_numbers)

# Output:
# [100  20  30  40]
# [100  20  30  40]