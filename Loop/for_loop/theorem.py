#------------------------------------------------------------------------------------------------#
# Structure-1: for loop with range(stop)
# for <variable> in <iterable>:
#    <statement>

# variable: The loop variable that takes each value from the iterable.
# iterable: A sequence (list, tuple, string, range, etc.) or any object that can return its elements one at a time
#------------------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------------------------#

#Example-1
for i in range(5):
    print("Hello")

#Example-2
for i in range(5):
    print(i)

#Example-3
for i in range(10):
    print(i)

#Example-4
word = "Python"
for char in word:
    print(char)


#------------------------------------------------------------------------------------------------#
# Structure-2: for loop with range(start, stop)
# for variable in range(start, stop):
#    <statement>
#------------------------------------------------------------------------------------------------#

#Example-1
for i in range(1,6):
    print(i)

#Example-2
for i in range(2,6):
    print(i)


#------------------------------------------------------------------------------------------------#
# Structure-3: for Loop with User Input
# <variable> = input("<prompt>")
# for <loop_variable> in <iterable>:
#     <statement>
#------------------------------------------------------------------------------------------------#

#Example-1
number = int(input("Enter a number: "))
for i in range(1, 11):
    print(number * i)


#------------------------------------------------------------------------------------------------#
#  Structure-4: for loop with range(start, stop, step)
# for variable in range range(start, stop):
#    <statement>
#------------------------------------------------------------------------------------------------#

#Example-1
for i in range(2,6,1):
    print(i)

#Example-2
for i in range(2,6,3):
    print(i)


#------------------------------------------------------------------------------------------------#
# Structure-5: for loop with enumerate()
# for index, value in enumerate(iterable):
#     <statement>
#------------------------------------------------------------------------------------------------#

#Example-1
for index, value in enumerate(["a", "b", "c"]):
    print(index, value)


#------------------------------------------------------------------------------------------------#
# Structure-6: Iterating Over a List Using for Loop
# list_name = [value1, value2, value3, ...]
# for <variable> in <list_name>:
#     <statement>
#------------------------------------------------------------------------------------------------#

#Example-1
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#Example-2
fruits = ["apple", "banana", "cherry"]
for index, value in enumerate(fruits):
    print(index, value)

#Example-3 Using enumerate() with start=1
fruits = ["apple", "banana", "cherry"]
for index, value in enumerate(fruits, start=1):
    print(index, value)


# Example-4: Using enumerate() with start=1
fruits = ["apple", "banana", "cherry"]
for index, value in enumerate(fruits, start=1):
    print(index, value)


#------------------------------------------------------------------------------------------------#
# Structure-7: General Nested for Loop
# for <variable1> in <iterable1>:
#     for <variable2> in <iterable2>:
#         <statement>
#------------------------------------------------------------------------------------------------#

# Example-1
for i in range(3):
    for j in range(2):
        print(i, j)


#------------------------------------------------------------------------------------------------#
# Structure-8: Nested for Loop
# list1 = [value1, value2, value3, ...]
# list2 = [value1, value2, value3, ...]
# for <variable1> in <list1>:
#     for <variable2> in <list2>:
#         <statement>
#------------------------------------------------------------------------------------------------#

# Example-1
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)

