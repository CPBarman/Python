#------------------------------------------------------------------------------------------------#
# Structure-1: continue Statement in for Loop
# for <variable> in <iterable>:
#     if <condition>:
#         continue
#     <statement>
#------------------------------------------------------------------------------------------------#


# Example-1: Skip a Specific Number
for i in range(1, 11):
    if i == 5:
        continue
    print(i)


#------------------------------------------------------------------------------------------------#
# Structure-2: continue Statement with input() in for Loop
# <variable> = int(input("<prompt>"))
# for <loop_variable> in range(<start>, <variable> + 1):
#     if <condition>:
#         continue
#     <statement>
#------------------------------------------------------------------------------------------------#

# Example-1: Skip Even Numbers
number = int(input("Enter a number: "))
for i in range(1, number + 1):
    if i % 2 == 0:
        continue
    print(i)

#Example-2: Using continue with input()
number = int(input("Enter a number: "))
for i in range(1, number + 1):
    if i % 2 == 0:
        continue
    print(i)


#------------------------------------------------------------------------------------------------#
# Structure-3: continue Statement with a List in for Loop
# <list_name> = [value1, value2, value3, ...]
# for <variable> in <list_name>:
#     if <condition>:
#         continue
#     <statement>
#------------------------------------------------------------------------------------------------#

# Example: Skip Negative Numbers
numbers = [10, -5, 20, -3, 30, -8]
for number in numbers:
    if number < 0:
        continue
    print(number)