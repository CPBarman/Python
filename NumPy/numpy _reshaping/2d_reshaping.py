#================================================================================================#
#                                       2D Reshaping


# Total Elements = Product of all Dimensions

# For 1D:
# size = n

# For 2D:
# size = rows × columns

# For 3D:
# size = layers × rows × columns


#Example
# Total number of elements must remain the same.

# Example:
# 6 elements → reshape(2, 3)     → 2 × 3 = 6   
# 6 elements → reshape(3, 2)     → 3 × 2 = 6   
# 6 elements → reshape(1, 6)     → 1 × 6 = 6   
# 6 elements → reshape(2, 3, 1) → 2 × 3 × 1 = 6 
# 6 elements → reshape(2, 2)     → 2 × 2 = 4   
# Reshaping is used to change the shape of an array without changing
# the total number of elements in the array.
#================================================================================================#




#------------------------------------------------------------------------------------------------#
# Structure-1: Reshaping a 2D Array into Another 2D Array
# <new_array> = <array_name>.reshape(<new_rows>, <new_columns>)
#------------------------------------------------------------------------------------------------#

# Example
import numpy as np
numbers = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
new_numbers = numbers.reshape(3, 2)
print(new_numbers)

# Output:
# [[10 20]
#  [30 40]
#  [50 60]]


#------------------------------------------------------------------------------------------------#
# Structure-2: Reshaping a 2D Array into a 1D Array
# <new_array> = <array_name>.reshape(<size>)
#------------------------------------------------------------------------------------------------#

# Example
import numpy as np
numbers = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
new_numbers = numbers.reshape(6)
print(new_numbers)

# Output:
# [10 20 30 40 50 60]


#------------------------------------------------------------------------------------------------#
# Structure-3: Reshaping a 2D Array into a 3D Array
# <new_array> = <array_name>.reshape(<layers>, <rows>, <columns>)
#------------------------------------------------------------------------------------------------#

# Example
import numpy as np
numbers = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
new_numbers = numbers.reshape(1, 2, 3)
print(new_numbers)

# Output:
# [[[10 20 30]
#   [40 50 60]]]


#------------------------------------------------------------------------------------------------#
# Structure-4: Checking the Shape After Reshaping
# <new_array>.shape
#------------------------------------------------------------------------------------------------#

# Example
import numpy as np
numbers = np.array([10, 20, 30, 40, 50, 60])
new_numbers = numbers.reshape(2, 3)
print(new_numbers.shape)

# Output:
# (2, 3)



