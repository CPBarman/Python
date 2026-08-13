#------------------------------------------------------------------------------------------------#
# Structure-1: Basic Syntax of if statement
# if condition:
#    statement
# elif condition:
#    statement
# else:
#    statement  
#------------------------------------------------------------------------------------------------#

# Example-1
age = 20
if age >= 18:
    print("You are adult.")
elif age >=13:
    print("You are teenager.")
else:
    print("You are child.")



#------------------------------------------------------------------------------------------------#
# Structure-2: if Statement with User Input
# user_input = type(input("Input Name: "))
# if user_input condition:
#    statement
# elif user_input condition:
#    statement
# else user_input condition:
#    statement
#------------------------------------------------------------------------------------------------#

#Example-1
age = int(input("Enter your age: "))
if age >= 18:
    print("You are adalt.")
elif age >= 13:
    print("You are teenager.")
else:
    print("You are child.")

#Example-2
mark = int(input("Enter your mark: "))
if mark >= 80:
    print("You got A+")
elif mark >= 70:
    print("You got A")
elif mark >= 60:
    print("You Passed")
else:
    print("You failed")