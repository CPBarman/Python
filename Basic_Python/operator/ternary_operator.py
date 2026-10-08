#================================================================================================#
#                              Conditional / Ternary Operator

# Conditional / Ternary operator is used to choose one of two values based on a condition
#
# It is a short form of a simple if-else statement
#
# Syntax:
# <value_if_true> if <condition> else <value_if_false>
#================================================================================================#




#------------------------------------------------------------------------------------------------#
# Structure-1: Basic Conditional / Ternary Operator
# <value_if_true> if <condition> else <value_if_false>
#------------------------------------------------------------------------------------------------#

# Example-1
age = 20
result = "Adult" if age >= 18 else "Minor"
print(result)

# Output:
# Adult




#------------------------------------------------------------------------------------------------#
# Structure-2: Conditional Operator with Numbers
# <value_if_true> if <condition> else <value_if_false>
#------------------------------------------------------------------------------------------------#

# Example-2
x = 10
result = 100 if x > 5 else 50
print(result)

# Output:
# 100




#------------------------------------------------------------------------------------------------#
# Structure-3: Conditional Operator with Comparison
# <value_if_true> if <condition> else <value_if_false>
#------------------------------------------------------------------------------------------------#

# Example-3
a = 10
b = 20
larger = a if a > b else b
print(larger)

# Output:
# 20




#------------------------------------------------------------------------------------------------#
# Structure-4: Conditional Operator with Even and Odd Numbers
# <value_if_true> if <condition> else <value_if_false>
#------------------------------------------------------------------------------------------------#

# Example-4
number = 7
result = "Even" if number % 2 == 0 else "Odd"
print(result)

# Output:
# Odd




#------------------------------------------------------------------------------------------------#
# Structure-5: Conditional Operator with Positive and Negative Numbers
# <value_if_true> if <condition> else <value_if_false>
#------------------------------------------------------------------------------------------------#

# Example-5
number = -5
result = "Positive" if number > 0 else "Negative"
print(result)

# Output:
# Negative




#------------------------------------------------------------------------------------------------#
# Structure-6: Conditional Operator with String
# <value_if_true> if <condition> else <value_if_false>
#------------------------------------------------------------------------------------------------#

# Example-6
marks = 75
result = "Pass" if marks >= 40 else "Fail"
print(result)

# Output:
# Pass




#------------------------------------------------------------------------------------------------#
# Structure-7: Nested Conditional / Ternary Operator
# <value1> if <condition1> else <value2> if <condition2> else <value3>
#------------------------------------------------------------------------------------------------#

# Example-7
marks = 75
result = "Excellent" if marks >= 80 else "Good" if marks >= 60 else "Needs Improvement"
print(result)

# Output:
# Good
