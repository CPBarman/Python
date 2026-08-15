#------------------------------------------------------------------------------------------------#
# Structure-1: for Loop with if-elif-else Statement
# for <variable> in <iterable>:
#     if <condition-1>:
#         <statement>
#     elif <condition-2>:
#         <statement>
#     else:
#         <statement>
#------------------------------------------------------------------------------------------------#

#Example-1
marks = [95, 75, 55, 35]
for mark in marks:
    if mark >= 80:
        print(mark, "Grade A")
    elif mark >= 60:
        print(mark, "Grade B")
    elif mark >= 40:
        print(mark, "Grade C")
    else:
        print(mark, "Fail")


#------------------------------------------------------------------------------------------------#
# Structure-2: for Loop with if-elif-else Statement
# for <variable> in <iterable>:
#     if <condition-1>:
#         <statement>
#     elif <condition-2>:
#         <statement>
#     else:
#         <statement>
#------------------------------------------------------------------------------------------------#

# Example-1: Checking Grade Using User Input
number_of_students = int(input("Enter number of students: "))
for i in range(number_of_students):
    marks = int(input("Enter marks: "))
    if marks >= 80:
        print("Grade A")
    elif marks >= 60:
        print("Grade B")
    elif marks >= 40:
        print("Grade C")
    else:
        print("Fail")