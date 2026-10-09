#================================================================================================#
#                                Nested if-elif-else Statement

# A nested if-elif-else statement contains an if-elif-else statement inside another if-elif-else
# statement
#
# if     → Executes a block when the condition is True
# elif   → Checks another condition if the previous condition is False
# else   → Executes a block when all preceding conditions are False
#
# Nested if-elif-else statements are used to check multiple conditions at different levels
#================================================================================================#




#------------------------------------------------------------------------------------------------#
# Structure-1: Basic Nested if-elif-else Statement
# if <condition1>:
#     if <condition2>:
#         <statement1>
#     elif <condition3>:
#         <statement2>
#     else:
#         <statement3>
# else:
#     <statement4>
#------------------------------------------------------------------------------------------------#

# Example-1
age = 20
marks = 75

if age >= 18:
    if marks >= 80:
        print("Grade A")
    elif marks >= 60:
        print("Grade B")
    else:
        print("Grade C")
else:
    print("Not Eligible")

# Output:
# Grade B




#------------------------------------------------------------------------------------------------#
# Structure-2: Nested if-elif-else Statement with Outer elif
# if <condition1>:
#     <statement1>
# elif <condition2>:
#     if <condition3>:
#         <statement2>
#     elif <condition4>:
#         <statement3>
#     else:
#         <statement4>
# else:
#     <statement5>
#------------------------------------------------------------------------------------------------#

# Example-2
marks = 65

if marks >= 90:
    print("Excellent")
elif marks >= 60:
    if marks >= 70:
        print("Very Good")
    elif marks >= 65:
        print("Good")
    else:
        print("Average")
else:
    print("Needs Improvement")

# Output:
# Good




#------------------------------------------------------------------------------------------------#
# Structure-3: Nested if-elif-else Statement for Checking Positive, Negative and Zero
# if <condition1>:
#     if <condition2>:
#         <statement1>
#     elif <condition3>:
#         <statement2>
#     else:
#         <statement3>
# else:
#     <statement4>
#------------------------------------------------------------------------------------------------#

# Example-3
number = -5

if number != 0:
    if number > 0:
        print("Positive Number")
    elif number < 0:
        print("Negative Number")
    else:
        print("Zero")
else:
    print("Number is Zero")

# Output:
# Negative Number




#------------------------------------------------------------------------------------------------#
# Structure-4: Nested if-elif-else Statement for Finding the Largest of Three Numbers
# if <condition1>:
#     if <condition2>:
#         <statement1>
#     elif <condition3>:
#         <statement2>
#     else:
#         <statement3>
# elif <condition4>:
#     <statement4>
# else:
#     <statement5>
#------------------------------------------------------------------------------------------------#

# Example-4
a = 10
b = 25
c = 15

if a > b:
    if a > c:
        print("a is Largest")
    elif a == c:
        print("a and c are Equal")
    else:
        print("c is Largest")
elif b > c:
    print("b is Largest")
else:
    print("c is Largest")

# Output:
# b is Largest




#------------------------------------------------------------------------------------------------#
# Structure-5: Nested if-elif-else Statement for Grading
# if <condition1>:
#     if <condition2>:
#         <statement1>
#     elif <condition3>:
#         <statement2>
#     else:
#         <statement3>
# elif <condition4>:
#     <statement4>
# else:
#     <statement5>
#------------------------------------------------------------------------------------------------#

# Example-5
marks = 85

if marks >= 40:
    if marks >= 80:
        print("Grade A")
    elif marks >= 60:
        print("Grade B")
    else:
        print("Grade C")
elif marks >= 30:
    print("Supplementary Exam")
else:
    print("Fail")

# Output:
# Grade A




#------------------------------------------------------------------------------------------------#
# Structure-6: Nested if-elif-else Statement for Checking Admission Eligibility
# if <condition1>:
#     if <condition2>:
#         <statement1>
#     elif <condition3>:
#         <statement2>
#     else:
#         <statement3>
# elif <condition4>:
#     <statement4>
# else:
#     <statement5>
#------------------------------------------------------------------------------------------------#

# Example-6
age = 19
marks = 55

if age >= 18:
    if marks >= 75:
        print("Eligible for Direct Admission")
    elif marks >= 50:
        print("Eligible for Admission")
    else:
        print("Insufficient Marks")
elif age >= 16:
    print("Age Requirement Not Met")
else:
    print("Not Eligible")

# Output:
# Eligible for Admission




#------------------------------------------------------------------------------------------------#
# Structure-7: Nested if-elif-else Statement with Multiple Levels
# if <condition1>:
#     if <condition2>:
#         if <condition3>:
#             <statement1>
#         elif <condition4>:
#             <statement2>
#         else:
#             <statement3>
#     elif <condition5>:
#         <statement4>
#     else:
#         <statement5>
# else:
#     <statement6>
#------------------------------------------------------------------------------------------------#

# Example-7
age = 22
marks = 85
attendance = 70

if age >= 18:
    if marks >= 60:
        if attendance >= 75:
            print("Eligible for Admission")
        elif attendance >= 60:
            print("Provisionally Eligible")
        else:
            print("Insufficient Attendance")
    elif marks >= 40:
        print("Marks Requirement Partially Met")
    else:
        print("Failed")
else:
    print("Underage")

# Output:
# Provisionally Eligible