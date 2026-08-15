#------------------------------------------------------------------------------------------------#
# Structure-1: for Loop with if Condition
# for <variable> in <iterable>:
#     if <condition>:
#         <statement>
#------------------------------------------------------------------------------------------------#

#Example-1
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

#Example-2
numbers = [10, 25, 60, 45, 80, 30, 90]
for number in numbers:
    if number > 50:
        print(number)
        