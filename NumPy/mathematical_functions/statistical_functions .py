#================================================================================================#
#                              NumPy Statistical Functions

# np.sum()          → Sum of values
# np.mean()         → Arithmetic mean / Average
# np.median()       → Median value
# np.min()          → Minimum value
# np.max()          → Maximum value
# np.std()          → Standard deviation
# np.var()          → Variance
# np.percentile()   → Percentile
# np.quantile()     → Quantile
# np.average()      → Average / Weighted average
# np.ptp()          → Range (Maximum - Minimum)
#================================================================================================#
# NumPy provides various statistical functions to perform
# statistical calculations efficiently on NumPy arrays.




#================================================================================================#
# Structure-1: Sum
#================================================================================================#
# np.sum(array)
#
# Statement:
# The np.sum() function calculates the sum of all elements
# in the given NumPy array.
#
# Structure:
# np.sum(array)
#------------------------------------------------------------------------------------------------#

#Example
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
result = np.sum(arr)
print(result)

# Output:
# 150


#------------------------------------------------------------------------------------------------#
# Structure-2: Mean
#------------------------------------------------------------------------------------------------#
# np.mean(array)
#
# Statement:
# The np.mean() function calculates the arithmetic mean
# (average) of all elements in the given NumPy array.
#
# Mathematical Formula:
#
#             Sum of all values
# Mean = -----------------------------
#             Number of values
#
# Structure:
# np.mean(array)
#------------------------------------------------------------------------------------------------#

#Example
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
result = np.mean(arr)
print(result)

# Output:
# 30.0


#------------------------------------------------------------------------------------------------#
# Structure-3: Median
#------------------------------------------------------------------------------------------------#
# np.median(array)
#
# Statement:
# The np.median() function calculates the median value
# of the given NumPy array.
#
# Structure:
# np.median(array)
#
# Note:
# For an odd number of values, the middle value is the median.
#
# For an even number of values, the average of the two middle
# values is the median.
#------------------------------------------------------------------------------------------------#

#Example
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
result = np.median(arr)
print(result)

# Output:
# 30.0


#------------------------------------------------------------------------------------------------#
# Structure-4: Minimum
#------------------------------------------------------------------------------------------------#
# np.min(array)
#
# Statement:
# The np.min() function returns the smallest value
# from the given NumPy array.
#
# Structure:
# np.min(array)
#------------------------------------------------------------------------------------------------#

#Example
import numpy as np
arr = np.array([10, 25, 5, 40, 15])
result = np.min(arr)
print(result)

# Output:
# 5


#------------------------------------------------------------------------------------------------#
# Structure-5: Maximum
#------------------------------------------------------------------------------------------------#
# np.max(array)
#
# Statement:
# The np.max() function returns the largest value
# from the given NumPy array.
#
# Structure:
# np.max(array)
#------------------------------------------------------------------------------------------------#

#Example
import numpy as np
arr = np.array([10, 25, 5, 40, 15])
result = np.max(arr)
print(result)

# Output:
# 40


#------------------------------------------------------------------------------------------------#
# Structure-6: Standard Deviation
#------------------------------------------------------------------------------------------------#
# np.std(array)
#
# Statement:
# The np.std() function calculates the standard deviation
# of the elements in the given NumPy array.
#
# Standard deviation measures how much the values
# are spread out from the mean.
#
# Structure:
# np.std(array)
#------------------------------------------------------------------------------------------------#

#Example
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
result = np.std(arr)
print(result)

# Output:
# 14.142135623730951


#------------------------------------------------------------------------------------------------#
# Structure-7: Variance
#------------------------------------------------------------------------------------------------#
# np.var(array)
#
# Statement:
# The np.var() function calculates the variance
# of the elements in the given NumPy array.
#
# Variance is the square of the standard deviation.
#
# Structure:
# np.var(array)
#------------------------------------------------------------------------------------------------#

#Example
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
result = np.var(arr)
print(result)

# Output:
# 200.0


#------------------------------------------------------------------------------------------------#
# Structure-8: Percentile
#------------------------------------------------------------------------------------------------#
# np.percentile(array, percentile)
#
# Statement:
# The np.percentile() function calculates the value below
# which a given percentage of data falls.
#
# Structure:
# np.percentile(array, percentile)
#------------------------------------------------------------------------------------------------#

#Example
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
result = np.percentile(arr, 50)
print(result)

# Output:
# 30.0

# Note:
# 50th percentile is equal to the median.


#------------------------------------------------------------------------------------------------#
# Structure-9: Quantile
#------------------------------------------------------------------------------------------------#
# np.quantile(array, quantile)
#
# Statement:
# The np.quantile() function calculates the value below
# which a given proportion of data falls.
#
# Structure:
# np.quantile(array, quantile)
#
# Quantile values range from 0 to 1.
#------------------------------------------------------------------------------------------------#

#Example
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
result = np.quantile(arr, 0.5)
print(result)

# Output:
# 30.0

# Note:
# 0.5 quantile is equal to the 50th percentile.


#------------------------------------------------------------------------------------------------#
# Structure-10: Average
#------------------------------------------------------------------------------------------------#
# np.average(array)
#
# Statement:
# The np.average() function calculates the weighted or
# unweighted average of elements in a NumPy array.
#
# Structure:
# np.average(array)
#------------------------------------------------------------------------------------------------#

#Example
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
result = np.average(arr)
print(result)

# Output:
# 30.0


#------------------------------------------------------------------------------------------------#
# Structure-11: Weighted Average
#------------------------------------------------------------------------------------------------#
# np.average(array, weights=weights)
#
# Statement:
# The np.average() function can calculate a weighted average
# when weights are provided.
#
# Structure:
# np.average(array, weights=weights)
#------------------------------------------------------------------------------------------------#

#Example
import numpy as np
arr = np.array([10, 20, 30])
weights = np.array([1, 2, 3])
result = np.average(arr, weights=weights)
print(result)

# Output:
# 23.333333333333332


#------------------------------------------------------------------------------------------------#
# Structure-12: Peak-to-Peak Range
#------------------------------------------------------------------------------------------------#
# np.ptp(array)
#
# Statement:
# The np.ptp() function calculates the difference between
# the maximum and minimum values of an array.
#
# Mathematical Formula:
#
# Range = Maximum Value - Minimum Value
#
# Structure:
# np.ptp(array)
#------------------------------------------------------------------------------------------------#

#Example
import numpy as np
arr = np.array([10, 20, 30, 40, 50])
result = np.ptp(arr)
print(result)

# Output:
# 40


#================================================================================================#
#                         Statistical Functions with Axis
#================================================================================================#

#------------------------------------------------------------------------------------------------#
# Structure-13: Sum Along an Axis
#------------------------------------------------------------------------------------------------#
# np.sum(array, axis=0)
# np.sum(array, axis=1)
#
# Statement:
# The axis parameter specifies the direction along which
# the statistical operation should be performed.
#
# axis=0 → Column-wise operation
# axis=1 → Row-wise operation
#------------------------------------------------------------------------------------------------#

#Example
import numpy as np
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
result_column = np.sum(arr, axis=0)
result_row = np.sum(arr, axis=1)
print(result_column)
print(result_row)

# Output:
# [50 70 90]
# [ 60 150]


#------------------------------------------------------------------------------------------------#
# Structure-14: Mean Along an Axis
#------------------------------------------------------------------------------------------------#
# np.mean(array, axis=0)
# np.mean(array, axis=1)
#
# Statement:
# The axis parameter can also be used with np.mean()
# to calculate column-wise or row-wise mean.
#------------------------------------------------------------------------------------------------#

#Example
import numpy as np
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
result_column = np.mean(arr, axis=0)
result_row = np.mean(arr, axis=1)
print(result_column)
print(result_row)

# Output:
# [25. 35. 45.]
# [20. 50.]


#------------------------------------------------------------------------------------------------#
# Structure-15: Median Along an Axis
#------------------------------------------------------------------------------------------------#
# np.median(array, axis=0)
# np.median(array, axis=1)
#
# Statement:
# The axis parameter can be used with np.median()
# to calculate the median column-wise or row-wise.
#------------------------------------------------------------------------------------------------#

#Example
import numpy as np
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
result_column = np.median(arr, axis=0)
result_row = np.median(arr, axis=1)
print(result_column)
print(result_row)

# Output:
# [25. 35. 45.]
# [20. 50.]

