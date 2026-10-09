#================================================================================================#
#                                  Nested if Statement

# A nested if statement is an if statement placed inside another if statement

# The inner if statement executes only when the outer if condition is True

# An else block can also be used inside a nested if statement
#================================================================================================#




#------------------------------------------------------------------------------------------------#
# Structure-1: Basic Nested if Statement
# if <condition1>:
#     if <condition2>:
#         <statement>
#------------------------------------------------------------------------------------------------#

# Example-1
age = 20
marks = 75

if age >= 18:
    if marks >= 40:
        print("Eligible")

# Output:
# Eligible




#------------------------------------------------------------------------------------------------#
# Structure-2: Nested if Statement with Inner else
# if <condition1>:
#     if <condition2>:
#         <statement1>
#     else:
#         <statement2>
#------------------------------------------------------------------------------------------------#

# Example-2
age = 20
marks = 30

if age >= 18:
    if marks >= 40:
        print("Pass")
    else:
        print("Fail")

# Output:
# Fail




#------------------------------------------------------------------------------------------------#
# Structure-3: Nested if Statement with Outer else
# if <condition1>:
#     if <condition2>:
#         <statement1>
#     else:
#         <statement2>
# else:
#     <statement3>
#------------------------------------------------------------------------------------------------#

# Example-3
age = 16
marks = 75

if age >= 18:
    if marks >= 40:
        print("Eligible")
    else:
        print("Not Eligible: Failed")
else:
    print("Not Eligible: Underage")

# Output:
# Not Eligible: Underage




#------------------------------------------------------------------------------------------------#
# Structure-4: Nested if Statement with Multiple Conditions
# if <condition1>:
#     if <condition2>:
#         if <condition3>:
#             <statement>
#------------------------------------------------------------------------------------------------#

# Example-4
age = 22
marks = 85
attendance = 90

if age >= 18:
    if marks >= 60:
        if attendance >= 75:
            print("Eligible for Admission")

# Output:
# Eligible for Admission




#------------------------------------------------------------------------------------------------#
# Structure-5: Nested if Statement for Checking Positive and Even Numbers
# if <condition1>:
#     if <condition2>:
#         <statement1>
#     else:
#         <statement2>
# else:
#     <statement3>
#------------------------------------------------------------------------------------------------#

# Example-5
number = 8

if number > 0:
    if number % 2 == 0:
        print("Positive Even Number")
    else:
        print("Positive Odd Number")
else:
    print("Number is Not Positive")

# Output:
# Positive Even Number




#------------------------------------------------------------------------------------------------#
# Structure-6: Nested if Statement for Finding the Largest of Three Numbers
# if <condition1>:
#     if <condition2>:
#         <statement1>
#     else:
#         <statement2>
# else:
#     if <condition3>:
#         <statement3>
#     else:
#         <statement4>
#------------------------------------------------------------------------------------------------#

# Example-6
a = 10
b = 25
c = 15

if a > b:
    if a > c:
        print("a is Largest")
    else:
        print("c is Largest")
else:
    if b > c:
        print("b is Largest")
    else:
        print("c is Largest")

# Output:
# b is Largest




#------------------------------------------------------------------------------------------------#
# Structure-7: Nested if Statement with Logical Operators
# if <condition1> and <condition2>:
#     if <condition3> or <condition4>:
#         <statement>
#------------------------------------------------------------------------------------------------#

# Example-7
age = 20
marks = 80
attendance = 85

if age >= 18 and marks >= 40:
    if attendance >= 75 or marks >= 90:
        print("Qualified")

# Output:
# Qualified
