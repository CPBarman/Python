#================================================================================================#
#                                  Identity Operators

# Identity operators are used to check whether two variables refer to the same object in memory
#
# is      → Returns True if both variables refer to the same object
# is not  → Returns True if both variables do not refer to the same object
#================================================================================================#




#------------------------------------------------------------------------------------------------#
# Structure-1: Identity Operator "is"
# <variable1> is <variable2>
#------------------------------------------------------------------------------------------------#

# Example-1
x = [10, 20, 30]
y = x

print(x is y)

# Output:
# True




#------------------------------------------------------------------------------------------------#
# Structure-2: Identity Operator "is not"
# <variable1> is not <variable2>
#------------------------------------------------------------------------------------------------#

# Example-2
x = [10, 20, 30]
y = [10, 20, 30]

print(x is not y)

# Output:
# True




#------------------------------------------------------------------------------------------------#
# Structure-3: Comparing Two Different Objects Using "is"
# <variable1> is <variable2>
#------------------------------------------------------------------------------------------------#

# Example-3
x = [10, 20, 30]
y = [10, 20, 30]

print(x is y)

# Output:
# False




#------------------------------------------------------------------------------------------------#
# Structure-4: Comparing Two Different Objects Using "is not"
# <variable1> is not <variable2>
#------------------------------------------------------------------------------------------------#

# Example-4
x = [10, 20, 30]
y = [10, 20, 30]

print(x is not y)

# Output:
# True




#------------------------------------------------------------------------------------------------#
# Structure-5: Identity Operators with None
# <variable> is None
#------------------------------------------------------------------------------------------------#

# Example-5
x = None
print(x is None)

# Output:
# True




#------------------------------------------------------------------------------------------------#
# Structure-6: Checking Whether a Variable is Not None
# <variable> is not None
#------------------------------------------------------------------------------------------------#

# Example-6
x = 10
print(x is not None)

# Output:
# True




#------------------------------------------------------------------------------------------------#
# Structure-7: Identity Operator with the Same Object
# <variable1> is <variable2>
#------------------------------------------------------------------------------------------------#

# Example-7
numbers = [10, 20, 30]
a = numbers
b = numbers

print(a is b)

# Output:
# True




#------------------------------------------------------------------------------------------------#
# Structure-8: Identity Operator with Different Objects
# <variable1> is <variable2>
#------------------------------------------------------------------------------------------------#

# Example-8
a = [10, 20, 30]
b = [10, 20, 30]

print(a is b)
print(a == b)

# Output:
# False
# True

