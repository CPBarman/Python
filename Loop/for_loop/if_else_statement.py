#------------------------------------------------------------------------------------------------#
# Structure-6: for Loop with if Condition
# for <variable> in <iterable>:
#     if <condition>:
#         <statement>
#     else:
#         <statement>
#------------------------------------------------------------------------------------------------#

# Example-1: Checking Even and Odd Numbers
for i in range(1, 6):
    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")


#------------------------------------------------------------------------------------------------#
# Structure-6: for Loop with if-else and input()
# number = int(input("<prompt>"))
# for <variable> in range(number):
#     if <condition>:
#         <statement>
#     else:
#         <statement>
#------------------------------------------------------------------------------------------------#

#Example-1
number = int(input("Enter a number: "))
for i in range(1, number + 1):
    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")