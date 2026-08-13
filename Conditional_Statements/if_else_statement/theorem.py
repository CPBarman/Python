#------------------------------------------------------------------------------------------------#
# Structure-1: Basic Syntax of if statement
# if condition:
#    statement
# else:
#    Statement
#------------------------------------------------------------------------------------------------#

# Example-1
age = 16
if age >= 18:
    print("You are adult")
else:
    print("You are not an adult")    

#Example-2
x = 4
if x > 5:
    print ("x is greater than 5")
else:
    print("x is less than or equal to 5")    

#Example-3
temperature = 10
if temperature > 30:
    print("Temperature is high.")
else:
    print("Temperature is normal or low.")    

#Example-4
age = 18
if age >= 18:
    print("You are an adult.")
    print("You are eligible for certain activities.")
else:
    print("You are not an adult.")     

#Example-5
marks = 35
if marks >= 40:
    print("You passed.") 
else:
    print("You failed.")    


#------------------------------------------------------------------------------------------------#
# Structure-2: if Statement with User Input
# user_input = type(input("Input Name: "))
# if user_input condition:
#    statement
# else:
#    Statement
#------------------------------------------------------------------------------------------------#

#Example-1
number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive")
else:
    print("The number is zero or negative")    

#Example-2
age =int(input("Enter your age: "))
if age >= 18:
    print("You are adult.")
else:
    print("You are not an  adult.")    

#Example-3
x = float(input("Enter a floating number: "))
if x > 0.0:
    print("The number is positive and greater than zero.")
else:
    print("The number is zero or negative.")    

#Example-4
temp = float(input("Enter the temperature: "))
if temp > 30:
    print("Temperature is high.")
else:
    print("Temperature is normal or low.")
