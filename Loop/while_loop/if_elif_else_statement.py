#------------------------------------------------------------------------------------------------#
# Structure-1: while Loop with if-elif-else Statement
# <initialization>
# while <condition>:
#     if <condition-1>:
#         <statement>
#     elif <condition-2>:
#         <statement>
#     else:
#         <statement>
#     <update>
#------------------------------------------------------------------------------------------------#

# Example-1: Checking Positive, Negative and Zero
i = 1
while i <= 5:
    number = int(input("Enter a number: "))

    if number > 0:
        print(number, "is Positive")
    elif number < 0:
        print(number, "is Negative")
    else:
        print(number, "is Zero")
    i += 1
    