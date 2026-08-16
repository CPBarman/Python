#------------------------------------------------------------------------------------------------#
# Structure-1: Creating a NumPy Array
# import numpy as <alias>
# <array_name> = np.array([value1, value2, value3, ...])
#------------------------------------------------------------------------------------------------#

# Example-1
import numpy as np
numbers = np.array([10, 20, 30, 40, 50])
print(numbers)               #[10 20 30 40 50]


# Example-2: Checking the Type of a NumPy Array
import numpy as np
numbers = np.array([10, 20, 30, 40, 50])
print(type(numbers))          #<class 'numpy.ndarray'>

#Example-3
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))              #[1 2 3 4 5]  #<class 'numpy.ndarray'>

#Example-4
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr[0])                  # 1

#Example-5
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr[2] + arr[3])           # 7

#------------------------------------------------------------------------------------------------#
# Structure-2: Finding the Number of Dimensions of an Array
# <array_name>.ndim
# ndim  = Number of Dimensions
# shape = Size of Each Dimension
# size  = Total Number of Elements
#------------------------------------------------------------------------------------------------#

# Example-1: 1D Array
import numpy as np
numbers = np.array([10, 20, 30, 40, 50])
print(numbers.ndim)
print(numbers.shape)
print(numbers.size)

# Output:
# 1
# (5,)
# 5
