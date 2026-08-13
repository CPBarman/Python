#------------------------------------------------------------------------------------------------#
# Structure-1: Basic Syntax of if statement
# if condition:
#    statement
#------------------------------------------------------------------------------------------------#

# Example-1
age = 18
if age >= 18:
    print("You are adult")

#Example-2
x = 10
if x > 5:
    print ("x is greater than 5")




#------------------------------------------------------------------------------------------------#
# Structure-2: if Statement with User Input
# user_input = type(input("Input Name: "))
# if user_input condition:
#    statement
#------------------------------------------------------------------------------------------------#

#Example-1
number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive")

#Example-2
age =int(input("Enter your age: "))
if age >= 18:
    print("You are adult")

#Example-3
x = float(input("Enter a floating number: "))
if x > 0.0:
    print("The number is positive and greater than zero")
    