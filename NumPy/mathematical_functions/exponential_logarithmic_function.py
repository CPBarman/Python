# NumPy provides several functions for calculating exponential
# and logarithmic values efficiently on NumPy arrays.


#------------------------------------------------------------------------------------------------#
# Structure-1: Exponential Function
#------------------------------------------------------------------------------------------------#
# np.exp(array)
#
# Statement:
# The np.exp() function calculates e raised to the power of each
# element in the given NumPy array.
#
# Mathematical Form:
# e^x
#------------------------------------------------------------------------------------------------#

#Example
import numpy as np
arr = np.array([0, 1, 2, 3])
result = np.exp(arr)
print(result)

# Output:
# [ 1.          2.71828183  7.3890561  20.08553692]


#------------------------------------------------------------------------------------------------#
# Structure-2: Natural Logarithm
#------------------------------------------------------------------------------------------------#
# np.log(array)
#
# Statement:
# The np.log() function calculates the natural logarithm (base e)
# of each element in the given NumPy array.
#
# Mathematical Form:
# ln(x)
#------------------------------------------------------------------------------------------------#

#Example
import numpy as np
arr = np.array([1, np.e, np.e**2])
result = np.log(arr)
print(result)

# Output:
# [0. 1. 2.]


#------------------------------------------------------------------------------------------------#
# Structure-3: Base-2 Logarithm
#------------------------------------------------------------------------------------------------#
# np.log2(array)
#
# Statement:
# The np.log2() function calculates the base-2 logarithm
# of each element in the given NumPy array.
#
# Mathematical Form:
# log₂(x)
#------------------------------------------------------------------------------------------------#

#Example
import numpy as np
arr = np.array([1, 2, 4, 8, 16])
result = np.log2(arr)
print(result)

# Output:
# [0. 1. 2. 3. 4.]


#------------------------------------------------------------------------------------------------#
# Structure-4: Base-10 Logarithm
#------------------------------------------------------------------------------------------------#
# np.log10(array)
#
# Statement:
# The np.log10() function calculates the base-10 logarithm
# of each element in the given NumPy array.
#
# Mathematical Form:
# log₁₀(x)
#------------------------------------------------------------------------------------------------#

#Example
import numpy as np
arr = np.array([1, 10, 100, 1000])
result = np.log10(arr)
print(result)

# Output:
# [0. 1. 2. 3.]


#------------------------------------------------------------------------------------------------#
# Structure-5: Exponential Minus One
#------------------------------------------------------------------------------------------------#
# np.expm1(array)
#
# Statement:
# The np.expm1() function calculates e^x - 1 for each element
# in the given NumPy array.
#
# Mathematical Form:
# e^x - 1
#------------------------------------------------------------------------------------------------#

#Example
import numpy as np
arr = np.array([0, 1, 2])
result = np.expm1(arr)
print(result)

# Output:
# [0.         1.71828183 6.3890561 ]


