#------------------------------------------------------------------------------------------------#
# Structure-1: break Statement in for Loop
# for <variable> in <iterable>:
#     if <condition>:
#         break
#     <statement>
#------------------------------------------------------------------------------------------------#

# Example-1: Stop the Loop at a Specific Value
for i in range(1, 11):
    if i == 5:
        break
    print(i)




#------------------------------------------------------------------------------------------------#
# Structure-2: for Loop with if-else and input()
# number = int(input("<prompt>"))
# for <variable> in range(number):
#     if <condition>:
#         break
#     <statement>
#------------------------------------------------------------------------------------------------#

# Example-1: Using break with input()
number = int(input("Enter a number: "))
for i in range(1, 11):
    if i == number:
        break
    print(i)