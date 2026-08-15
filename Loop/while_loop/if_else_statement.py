#------------------------------------------------------------------------------------------------#
# Structure-1: while Loop with if-else Statement
# <initialization>
# while <condition>:
#     if <condition>:
#         <statement>
#     else:
#         <statement>
#     <update>
#------------------------------------------------------------------------------------------------#

# Example
i = 1
while i <= 5:
    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")
    i += 1
