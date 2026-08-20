#================================================================================================#
#                                    NumPy Array 

# np.ndim   → Returns the number of dimensions of an array
# np.size   → Returns the total number of elements in an array
# np.shape  → Returns the dimensions of an array
# np.dtype  → Returns the data type of array elements
#================================================================================================#



#------------------------------------------------------------------------------------------------#
# Structure-1: Creating a NumPy Array
# import numpy as <alias>
# <array_name> = np.array([value1, value2, value3, ...])
#------------------------------------------------------------------------------------------------#

# Example-1
import numpy as np
numbers = np.array([10, 20, 30, 40, 50])
print(numbers) 

# Output:
# [10 20 30 40 50]


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

# Example-3: Checking the Type of a NumPy Array
import numpy as np
numbers = np.array([10, 20, 30, 40, 50])
print(type(numbers))          

# Output:
#<class 'numpy.ndarray'>

#Example-4
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))              

# Output:
#[1 2 3 4 5]  #<class 'numpy.ndarray'>


# Example-5: Finding the Data Type of a Boolean Array
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
