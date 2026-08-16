#------------------------------------------------------------------------------------------------#
# Structure-1: Basic while Loop
# <initialization>
# while <condition>:
#     <statement>
#     <update>
#------------------------------------------------------------------------------------------------#

# Example-1
i = 1
while i <= 5:
    print("Hello")
    i += 1

# Example-2
i = 1
while i <= 5:
    print(i)
    i += 1


#------------------------------------------------------------------------------------------------#
# Structure-2: while Loop with User Input
# <variable> = input("<prompt>")
# while <condition>:
#     <statement>
#     <update>
#------------------------------------------------------------------------------------------------#

# Example
number = int(input("Enter a number: "))
i = 1
while i <= number:
    print(i)
    i += 1

