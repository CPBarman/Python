#------------------------------------------------------------------------------------------------#
# Structure-1: Reshaping a NumPy Array
# <new_array> = <array_name>.reshape(<rows>, <columns>)
#------------------------------------------------------------------------------------------------#

# Example
import numpy as np
numbers = np.array([10, 20, 30, 40, 50, 60])
new_numbers = numbers.reshape(2, 3)
print(new_numbers)

# Output:
# [[10 20 30]
# [40 50 60]]


#Example
import numpy as np
num = np.array([10, 20, 30, 40, 50, 60])
numbers = num.reshape(3, 2)
print(numbers)

# Output:
# [[10 20]
# [30 40]
# [50 60]]


#------------------------------------------------------------------------------------------------#
# Structure-2: Reshaping a 1D Array into a 3D Array
# <new_array> = <array_name>.reshape(<layers>, <rows>, <columns>)
#------------------------------------------------------------------------------------------------#

# Example
import numpy as np
numbers = np.array([10, 20, 30, 40, 50, 60, 70, 80])
new_numbers = numbers.reshape(2, 2, 2)
print(new_numbers)

# Output:
# [[[10 20]
# [30 40]]

# [[50 60]
# [70 80]]]


#------------------------------------------------------------------------------------------------#
# Structure-3: Checking the Shape After Reshaping
# <array_name>.shape
#------------------------------------------------------------------------------------------------#

# Example
import numpy as np
numbers = np.array([10, 20, 30, 40, 50, 60])
new_numbers = numbers.reshape(2, 3)
print(new_numbers.shape)

# Output:
# (2, 3)


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



#------------------------------------------------------------------------------------------------#
# Structure-12: Using -1 for Automatic Dimension
# <new_array> = <array_name>.reshape(<known_dimension>, -1)
#------------------------------------------------------------------------------------------------#

# Example
import numpy as np
numbers = np.array([10, 20, 30, 40, 50, 60])
new_numbers = numbers.reshape(2, -1)
print(new_numbers)

# Output:
# [[10 20 30]
#  [40 50 60]]


# Example-2
numbers = np.array([10, 20, 30, 40, 50, 60])
new_numbers = numbers.reshape(-1, 2)
print(new_numbers)

# Output:
# [[10 20]
# [30 40]
# [50 60]]