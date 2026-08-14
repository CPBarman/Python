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

#Example
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