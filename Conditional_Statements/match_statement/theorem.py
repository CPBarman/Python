#================================================================================================#
#                                  Match Statement

# The match statement is used to compare a value against multiple patterns
#
# It is similar to the switch statement in C
#
# match   → Evaluates the given subject
# case    → Checks a pattern against the subject
# _       → Acts as a wildcard pattern (default case)
#
# The match statement was introduced in Python 3.10
#================================================================================================#




#------------------------------------------------------------------------------------------------#
# Structure-1: Basic Match Statement
# match <value>:
#     case <pattern1>:
#         <statement1>
#     case <pattern2>:
#         <statement2>
#     case _:
#         <default_statement>
#------------------------------------------------------------------------------------------------#

# Example-1
day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case _:
        print("Invalid Day")

# Output:
# Wednesday




#------------------------------------------------------------------------------------------------#
# Structure-2: Match Statement with Default Case
# match <value>:
#     case <pattern1>:
#         <statement1>
#     case _:
#         <default_statement>
#------------------------------------------------------------------------------------------------#

# Example-2
number = 5

match number:
    case 1:
        print("One")
    case 2:
        print("Two")
    case _:
        print("Other Number")

# Output:
# Other Number




#------------------------------------------------------------------------------------------------#
# Structure-3: Match Statement with String Values
# match <string_variable>:
#     case "<value1>":
#         <statement1>
#     case "<value2>":
#         <statement2>
#     case _:
#         <default_statement>
#------------------------------------------------------------------------------------------------#

# Example-3
fruit = "Apple"

match fruit:
    case "Apple":
        print("Red Fruit")
    case "Banana":
        print("Yellow Fruit")
    case "Orange":
        print("Orange Fruit")
    case _:
        print("Unknown Fruit")

# Output:
# Red Fruit




#------------------------------------------------------------------------------------------------#
# Structure-4: Match Statement with Multiple Patterns
# match <value>:
#     case <pattern1> | <pattern2>:
#         <statement1>
#     case _:
#         <default_statement>
#------------------------------------------------------------------------------------------------#

# Example-4
day = 6

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Weekday")
    case 6 | 7:
        print("Weekend")
    case _:
        print("Invalid Day")

# Output:
# Weekend




#------------------------------------------------------------------------------------------------#
# Structure-5: Match Statement with a Variable
# match <value>:
#     case <variable>:
#         <statement>
#------------------------------------------------------------------------------------------------#

# Example-5
number = 10

match number:
    case 10:
        print("Number is Ten")
    case 20:
        print("Number is Twenty")
    case _:
        print("Unknown Number")

# Output:
# Number is Ten




#------------------------------------------------------------------------------------------------#
# Structure-6: Match Statement with if Guard
# match <value>:
#     case <pattern> if <condition>:
#         <statement1>
#     case _:
#         <statement2>
#------------------------------------------------------------------------------------------------#

# Example-6
number = 15

match number:
    case n if n > 0:
        print("Positive Number")
    case n if n < 0:
        print("Negative Number")
    case _:
        print("Zero")

# Output:
# Positive Number




#------------------------------------------------------------------------------------------------#
# Structure-7: Match Statement with Tuple Patterns
# match <tuple>:
#     case (<pattern1>, <pattern2>):
#         <statement1>
#     case _:
#         <default_statement>
#------------------------------------------------------------------------------------------------#

# Example-7
point = (0, 5)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print("On Y-axis")
    case (x, 0):
        print("On X-axis")
    case _:
        print("Somewhere Else")

# Output:
# On Y-axis




#------------------------------------------------------------------------------------------------#
# Structure-8: Match Statement with Multiple Values Using OR Pattern
# match <value>:
#     case <pattern1> | <pattern2> | <pattern3>:
#         <statement1>
#     case _:
#         <default_statement>
#------------------------------------------------------------------------------------------------#

# Example-8
grade = "B"

match grade:
    case "A" | "B":
        print("Good Grade")
    case "C" | "D":
        print("Average Grade")
    case "F":
        print("Fail")
    case _:
        print("Invalid Grade")

# Output:
# Good Grade