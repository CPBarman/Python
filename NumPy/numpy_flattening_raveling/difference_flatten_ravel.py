#================================================================================================#
#                               Difference between flatten() and ravel()

# flatten()
# <new_array> = <array_name>.flatten()
# → Returns a copy of the array.
# Converts a multi-dimensional array into a 1D array.
# Returns a copy.
# Changes in the new array do not affect the original array.


# ravel()
# <new_array> = <array_name>.ravel()
# → Returns a flattened array and may return a view when possible.
# Converts a multi-dimensional array into a 1D array.
# Returns a view when possible.
# Changes in the new array may affect the original array.
#================================================================================================#




#Example
import numpy as np
arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
flat = arr.flatten()
rav = arr.ravel()
print(flat)
print(rav)

# Output:
# [1 2 3 4 5 6]
# [1 2 3 4 5 6]

