#================================================================================================#
#                                Nested if-else Statement

# A nested if-else statement is an if-else statement placed inside another if-else statement
#
# The inner if-else statement executes based on the condition of the outer if-else statement
#
# if     → Executes a block when the condition is True
# else   → Executes a block when the condition is False
#================================================================================================#




#------------------------------------------------------------------------------------------------#
# Structure-1: Basic Nested if-else Statement
# if <condition1>:
#     if <condition2>:
#         <statement1>
#     else:
#         <statement2>
# else:
#     <statement3>
#------------------------------------------------------------------------------------------------#

# Example-1
age = 20
marks = 75

if age >= 18:
    if marks >= 40:
        print("Eligible and Passed")
    else:
        print("Eligible but Failed")
else:
    print("Not Eligible")

# Output:
# Eligible and Passed




#------------------------------------------------------------------------------------------------#
# Structure-2: Nested if-else Statement with Both Inner and Outer else
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

# Example-2
age = 16
marks = 35

if age >= 18:
    if marks >= 40:
        print("Adult and Passed")
    else:
        print("Adult but Failed")
else:
    if marks >= 40:
        print("Minor but Passed")
    else:
        print("Minor and Failed")

# Output:
# Minor and Failed




#------------------------------------------------------------------------------------------------#
# Structure-3: Nested if-else Statement for Checking Even and Odd Numbers
# if <condition1>:
#     if <condition2>:
#         <statement1>
#     else:
#         <statement2>
# else:
#     <statement3>
#------------------------------------------------------------------------------------------------#

# Example-3
number = 7

if number >= 0:
    if number % 2 == 0:
        print("Positive Even Number")
    else:
        print("Positive Odd Number")
else:
    print("Negative Number")

# Output:
# Positive Odd Number




#------------------------------------------------------------------------------------------------#
# Structure-4: Nested if-else Statement for Finding the Largest of Two Numbers
# if <condition1>:
#     if <condition2>:
#         <statement1>
#     else:
#         <statement2>
# else:
#     <statement3>
#------------------------------------------------------------------------------------------------#

# Example-4
a = 10
b = 20

if a != b:
    if a > b:
        print("a is Largest")
    else:
        print("b is Largest")
else:
    print("Both Numbers are Equal")

# Output:
# b is Largest




#------------------------------------------------------------------------------------------------#
# Structure-5: Nested if-else Statement for Finding the Largest of Three Numbers
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

# Example-5
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
# Structure-6: Nested if-else Statement for Checking Pass and Fail
# if <condition1>:
#     if <condition2>:
#         <statement1>
#     else:
#         <statement2>
# else:
#     <statement3>
#------------------------------------------------------------------------------------------------#

# Example-6
theory_marks = 55
practical_marks = 35

if theory_marks >= 40:
    if practical_marks >= 40:
        print("Pass")
    else:
        print("Fail in Practical")
else:
    print("Fail in Theory")

# Output:
# Fail in Practical




#------------------------------------------------------------------------------------------------#
# Structure-7: Nested if-else Statement with Multiple Conditions
# if <condition1>:
#     if <condition2>:
#         if <condition3>:
#             <statement1>
#         else:
#             <statement2>
#     else:
#         <statement3>
# else:
#     <statement4>
#------------------------------------------------------------------------------------------------#

# Example-7
age = 22
marks = 85
attendance = 60

if age >= 18:
    if marks >= 60:
        if attendance >= 75:
            print("Eligible for Admission")
        else:
            print("Insufficient Attendance")
    else:
        print("Insufficient Marks")
else:
    print("Underage")

# Output:
# Insufficient Attendance