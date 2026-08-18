#------------------------------------------------------------------------------------------------#
#                           Trigonometric Functions
#------------------------------------------------------------------------------------------------#
#
# NumPy provides various trigonometric functions to perform
# trigonometric calculations efficiently on NumPy arrays.
#
# Important:
# NumPy trigonometric functions use angles in radians.
#
# Degree to Radian:
# 0°   = 0
# 45°  = π / 4
# 90°  = π / 2
# 180° = π
#------------------------------------------------------------------------------------------------#




#------------------------------------------------------------------------------------------------#
# Structure-1: Sine Function
#------------------------------------------------------------------------------------------------#
# np.sin(array)
#
# Statement:
# The np.sin() function calculates the sine of each element
# in the given NumPy array.
#
# The input angles must be given in radians.
#------------------------------------------------------------------------------------------------#
# Example
import numpy as np
arr = np.array([0, np.pi / 2, np.pi])
result = np.sin(arr)
print(result)

# Output:
# [0.0000000e+00 1.0000000e+00 1.2246468e-16]

# Approximately:
# [0. 1. 0.]


#------------------------------------------------------------------------------------------------#
# Structure-2: Cosine Function
#------------------------------------------------------------------------------------------------#
# np.cos(array)
#
# Statement:
# The np.cos() function calculates the cosine of each element
# in the given NumPy array.
#
# The input angles must be given in radians.
#------------------------------------------------------------------------------------------------#

# Example
import numpy as np
arr = np.array([0, np.pi / 2, np.pi])
result = np.cos(arr)
print(result)

# Output:
# [ 1.000000e+00  6.123234e-17 -1.000000e+00]

# Approximately:
# [1. 0. -1.]


#------------------------------------------------------------------------------------------------#
# Structure-3: Tangent Function
#------------------------------------------------------------------------------------------------#
# np.tan(array)
#
# Statement:
# The np.tan() function calculates the tangent of each element
# in the given NumPy array.
#
# The input angles must be given in radians.
#------------------------------------------------------------------------------------------------#

# Example
import numpy as np
arr = np.array([0, np.pi / 4])
result = np.tan(arr)
print(result)

# Output:
# [0. 1.]


#------------------------------------------------------------------------------------------------#
# Structure-4: Inverse Sine Function
#------------------------------------------------------------------------------------------------#
# np.arcsin(array)
#
# Statement:
# The np.arcsin() function calculates the inverse sine
# (arcsine) of each element in the given NumPy array.
#
# The result is returned in radians.
#
# Input range:
# -1 ≤ x ≤ 1
#------------------------------------------------------------------------------------------------#

# Example
import numpy as np
arr = np.array([0, 1, -1])
result = np.arcsin(arr)
print(result)

# Output:
# [ 0.          1.57079633 -1.57079633]


#------------------------------------------------------------------------------------------------#
# Structure-5: Inverse Cosine Function
#------------------------------------------------------------------------------------------------#
# np.arccos(array)
#
# Statement:
# The np.arccos() function calculates the inverse cosine
# (arccosine) of each element in the given NumPy array.
#
# The result is returned in radians.
#
# Input range:
# -1 ≤ x ≤ 1
#------------------------------------------------------------------------------------------------#

# Example
import numpy as np
arr = np.array([1, 0, -1])
result = np.arccos(arr)
print(result)

# Output:
# [0.         1.57079633 3.14159265]


#------------------------------------------------------------------------------------------------#
# Structure-6: Inverse Tangent Function
#------------------------------------------------------------------------------------------------#
# np.arctan(array)
#
# Statement:
# The np.arctan() function calculates the inverse tangent
# (arctangent) of each element in the given NumPy array.
#
# The result is returned in radians.
#------------------------------------------------------------------------------------------------#

# Example
import numpy as np
arr = np.array([0, 1, -1])
result = np.arctan(arr)
print(result)

# Output:
# [ 0.          0.78539816 -0.78539816]


#------------------------------------------------------------------------------------------------#
# Structure-7: Hyperbolic Sine Function
#------------------------------------------------------------------------------------------------#
# np.sinh(array)
#
# Statement:
# The np.sinh() function calculates the hyperbolic sine
# of each element in the given NumPy array.
#------------------------------------------------------------------------------------------------#

# Example
import numpy as np
arr = np.array([0, 1, 2])
result = np.sinh(arr)
print(result)


#------------------------------------------------------------------------------------------------#
# Structure-8: Hyperbolic Cosine Function
#------------------------------------------------------------------------------------------------#
# np.cosh(array)
#
# Statement:
# The np.cosh() function calculates the hyperbolic cosine
# of each element in the given NumPy array.
#------------------------------------------------------------------------------------------------#

# Example
import numpy as np
arr = np.array([0, 1, 2])
result = np.cosh(arr)
print(result)


#------------------------------------------------------------------------------------------------#
# Structure-9: Hyperbolic Tangent Function
#------------------------------------------------------------------------------------------------#
# np.tanh(array)
#
# Statement:
# The np.tanh() function calculates the hyperbolic tangent
# of each element in the given NumPy array.
#------------------------------------------------------------------------------------------------#

# Example
import numpy as np
arr = np.array([0, 1, 2])
result = np.tanh(arr)
print(result)





#------------------------------------------------------------------------------------------------#
# 1. np.sin()       → Sine
# 2. np.cos()       → Cosine
# 3. np.tan()       → Tangent

# 4. np.arcsin()    → Inverse Sine
# 5. np.arccos()    → Inverse Cosine
# 6. np.arctan()    → Inverse Tangent

# 7. np.sinh()      → Hyperbolic Sine
# 8. np.cosh()      → Hyperbolic Cosine
# 9. np.tanh()      → Hyperbolic Tangent
#------------------------------------------------------------------------------------------------#
