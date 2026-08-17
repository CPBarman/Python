#------------------------------------------------------------------------------------------------#
# Structure-1: Accessing an Element Using Negative Index
# <array_name>[-<row_index>, -<column_index>]
#------------------------------------------------------------------------------------------------#

# Example
numbers = np.array([
    [10, 20, 30],
    [40, 50, 60]
])
print(numbers[-1, -1])
print(numbers[-2, -2])

# Output:
# 60
# 20