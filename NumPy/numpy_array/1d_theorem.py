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


#------------------------------------------------------------------------------------------------#
# Structure-2: Finding the Number of Dimensions of an Array
# <array_name>.ndim
# ndim  = Number of Dimensions
# shape = Size of Each Dimension (Number of Rows & Columns)
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

#------------------------------------------------------------------------------------------------#
# Structure-3: Finding the Data Type of an Array
# <array_name>.dtype
#------------------------------------------------------------------------------------------------#

# Example-1: Integer Array
import numpy as np
numbers = np.array([10, 20, 30, 40, 50])
print(numbers.dtype)

# Output:
# int64


# Example-2: Finding the Data Type of a Float Array
numbers = np.array([10.5, 20.5, 30.5])
print(numbers.dtype)
# Output:
# float64


# Example-3: Finding the Data Type of a Boolean Array
values = np.array([True, False, True])
print(values.dtype)
# Output:
# bool

#------------------------------------------------------------------------------------------------#
# Structure-4: Creating an Array with a Specific Data Type
# <array_name> = np.array([value1, value2, ...], dtype=<data_type>)
#------------------------------------------------------------------------------------------------#

# Example
import numpy as np
numbers = np.array([10, 20, 30, 40], dtype=np.float32)
print(numbers)
print(numbers.dtype)

# Output:
# [10. 20. 30. 40.]
# float32


#------------------------------------------------------------------------------------------------#
# Structure-11: Accessing an Element of a 1D Array Using Index
# <array_name>[<index>]
#------------------------------------------------------------------------------------------------#

# Example-1
import numpy as np
numbers = np.array([10, 20, 30, 40, 50])
print(numbers[0])
print(numbers[2])
print(numbers[4])

# Output:
# 10
# 30
# 50

#Example-2
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr[0])                  

# Output:
# 1

#Example-3
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr[2] + arr[3])          

# Output:
 # 7


