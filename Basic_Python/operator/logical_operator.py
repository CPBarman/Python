#================================================================================================#
#                                  Logical Operators

# Logical operators are used to combine or reverse Boolean conditions
#
# and  → Returns True if both conditions are True
# or   → Returns True if at least one condition is True
# not  → Reverses the result of a Boolean condition
#================================================================================================#




#------------------------------------------------------------------------------------------------#
# Structure-1: Logical AND Operator
# <condition1> and <condition2>
#------------------------------------------------------------------------------------------------#

# Example-1
x = 10
print(x > 5 and x < 20)

# Output:
# True




#------------------------------------------------------------------------------------------------#
# Structure-2: Logical OR Operator
# <condition1> or <condition2>
#------------------------------------------------------------------------------------------------#

# Example-2
x = 10
print(x < 5 or x < 20)

# Output:
# True




#------------------------------------------------------------------------------------------------#
# Structure-3: Logical NOT Operator
# not <condition>
#------------------------------------------------------------------------------------------------#

# Example-3
x = 10
print(not x > 5)

# Output:
# False




#------------------------------------------------------------------------------------------------#
# Structure-4: Using AND Operator with Two False Conditions
# <condition1> and <condition2>
#------------------------------------------------------------------------------------------------#

# Example-4
x = 10
print(x > 20 and x < 30)

# Output:
# False




#------------------------------------------------------------------------------------------------#
# Structure-5: Using OR Operator with Two False Conditions
# <condition1> or <condition2>
#------------------------------------------------------------------------------------------------#

# Example-5
x = 10
print(x > 20 or x < 5)

# Output:
# False




#------------------------------------------------------------------------------------------------#
# Structure-6: Using NOT Operator with a False Condition
# not <condition>
#------------------------------------------------------------------------------------------------#

# Example-6
x = 10
print(not x > 20)

# Output:
# True




#------------------------------------------------------------------------------------------------#
# Structure-7: Combining Multiple Logical Operators
# <condition1> and <condition2> or <condition3>
#------------------------------------------------------------------------------------------------#

# Example-7
x = 10
y = 20
print(x > 5 and y > 15 or x > 20)

# Output:
# True




#------------------------------------------------------------------------------------------------#
# Structure-8: Logical Operators with Variables
# <variable1> <operator> <variable2>
#------------------------------------------------------------------------------------------------#

# Example-8
age = 20
marks = 75

print(age >= 18 and marks >= 40)
print(age >= 18 or marks < 40)
print(not age < 18)

# Output:
# True
# True
# True

