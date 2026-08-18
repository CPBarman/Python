#------------------------------------------------------------------------------------------------#
#                              Rounding Functions

# 1. np.round()   → Round to nearest value
# 2. np.floor()   → Round down
# 3. np.ceil()    → Round up
# 4. np.trunc()   → Remove decimal part
#------------------------------------------------------------------------------------------------#
#
# Rounding functions are used to round numerical values in a
# NumPy array according to different rules.
#
#------------------------------------------------------------------------------------------------#




#------------------------------------------------------------------------------------------------#
# Structure-1: Round Function
#------------------------------------------------------------------------------------------------#
# np.round(array)
#
# Statement:
# The np.round() function rounds each element of the given
# NumPy array to the nearest value.
#
# Structure:
# np.round(array)
#
# We can also specify the number of decimal places:
# np.round(array, decimals)
#------------------------------------------------------------------------------------------------#

#Example
import numpy as np
arr = np.array([1.2, 2.5, 3.7, 4.9])
result = np.round(arr)
print(result)

# Output:
# [1. 2. 4. 5.]


#------------------------------------------------------------------------------------------------#
# Structure-2: Floor Function
#------------------------------------------------------------------------------------------------#
# np.floor(array)
#
# Statement:
# The np.floor() function rounds each element of the given
# NumPy array down to the nearest integer.
#
# Structure:
# np.floor(array)
#------------------------------------------------------------------------------------------------#

#Example
import numpy as np
arr = np.array([1.2, 2.8, 3.5, 4.9])
result = np.floor(arr)
print(result)

# Output:
# [1. 2. 3. 4.]


#------------------------------------------------------------------------------------------------#
# Structure-3: Ceil Function
#------------------------------------------------------------------------------------------------#
# np.ceil(array)
#
# Statement:
# The np.ceil() function rounds each element of the given
# NumPy array up to the nearest integer.
#
# Structure:
# np.ceil(array)
#------------------------------------------------------------------------------------------------#

#Example
import numpy as np
arr = np.array([1.2, 2.1, 3.5, 4.9])
result = np.ceil(arr)
print(result)

# Output:
# [2. 3. 4. 5.]


#------------------------------------------------------------------------------------------------#
# Structure-4: Truncate Function
#------------------------------------------------------------------------------------------------#
# np.trunc(array)
#
# Statement:
# The np.trunc() function removes the decimal part of each
# element in the given NumPy array.
#
# Structure:
# np.trunc(array)
#------------------------------------------------------------------------------------------------#

#Example
import numpy as np
arr = np.array([1.9, 2.7, -3.8, -4.2])
result = np.trunc(arr)
print(result)

# Output:
# [ 1.  2. -3. -4.]
