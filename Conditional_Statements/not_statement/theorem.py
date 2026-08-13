#------------------------------------------------------------------------------------------------#
# Structure-1: Basic Syntax of if statement
#  
#------------------------------------------------------------------------------------------------#

raining = False
if not raining:
    print("You can go outside")



#------------------------------------------------------------------------------------------------#
# Structure-2: if Statement with User Input
#  
#------------------------------------------------------------------------------------------------#

#Example-1
rain = input("Is it raining (yes/no): ")
if rain == "no":
    print("You can go outside")
else:
    print("You cannot go outside")
