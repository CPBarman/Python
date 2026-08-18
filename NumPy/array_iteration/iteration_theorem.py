#------------------------------------------------------------------------------------------------#
# Structure-1: Iterating Over a 1D NumPy Array
# for <variable> in <array_name>:
#     <statement>
#------------------------------------------------------------------------------------------------#

# Example
import numpy as np
numbers = np.array([10, 20, 30, 40, 50])
for number in numbers:
    print(number)

# Output:
# 10
# 20
# 30
# 40
# 50


#------------------------------------------------------------------------------------------------#
# Structure-2: Iterating Over a 2D NumPy Array
# for <row> in <array_name>:
#     <statement>
#------------------------------------------------------------------------------------------------#

# Example
import numpy as np
numbers = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
for row in numbers:
    print(row)

# Output:
# [10 20 30]
# [40 50 60]


#------------------------------------------------------------------------------------------------#
# Structure-3: Iterating Over Each Element of a 2D NumPy Array
# for <row> in <array_name>:
#     for <element> in <row>:
#         <statement>
#------------------------------------------------------------------------------------------------#

# Example
import numpy as np
numbers = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
for row in numbers:
    for number in row:
        print(number)

# Output:
# 10
# 20
# 30
# 40
# 50
# 60