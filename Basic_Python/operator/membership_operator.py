#================================================================================================#
#                                  Membership Operators

# Membership operators are used to check whether a value exists in a sequence
#
# in      → Returns True if a value is present in the sequence
# not in  → Returns True if a value is not present in the sequence
#================================================================================================#




#------------------------------------------------------------------------------------------------#
# Structure-1: Membership Operator "in"
# <value> in <sequence>
#------------------------------------------------------------------------------------------------#

# Example-1
numbers = [10, 20, 30, 40, 50]
print(30 in numbers)

# Output:
# True




#------------------------------------------------------------------------------------------------#
# Structure-2: Membership Operator "not in"
# <value> not in <sequence>
#------------------------------------------------------------------------------------------------#

# Example-2
numbers = [10, 20, 30, 40, 50]
print(60 not in numbers)

# Output:
# True




#------------------------------------------------------------------------------------------------#
# Structure-3: Using "in" with a String
# <substring> in <string>
#------------------------------------------------------------------------------------------------#

# Example-3
text = "Python Programming"
print("Python" in text)

# Output:
# True




#------------------------------------------------------------------------------------------------#
# Structure-4: Using "not in" with a String
# <substring> not in <string>
#------------------------------------------------------------------------------------------------#

# Example-4
text = "Python Programming"
print("Java" not in text)

# Output:
# True




#------------------------------------------------------------------------------------------------#
# Structure-5: Using "in" with a Tuple
# <value> in <tuple>
#------------------------------------------------------------------------------------------------#

# Example-5
fruits = ("Apple", "Banana", "Mango", "Orange")
print("Mango" in fruits)

# Output:
# True




#------------------------------------------------------------------------------------------------#
# Structure-6: Using "not in" with a Tuple
# <value> not in <tuple>
#------------------------------------------------------------------------------------------------#

# Example-6
fruits = ("Apple", "Banana", "Mango", "Orange")
print("Grapes" not in fruits)

# Output:
# True




#------------------------------------------------------------------------------------------------#
# Structure-7: Using "in" with a Set
# <value> in <set>
#------------------------------------------------------------------------------------------------#

# Example-7
numbers = {10, 20, 30, 40, 50}
print(20 in numbers)

# Output:
# True




#------------------------------------------------------------------------------------------------#
# Structure-8: Using "not in" with a Set
# <value> not in <set>
#------------------------------------------------------------------------------------------------#

# Example-8
numbers = {10, 20, 30, 40, 50}
print(60 not in numbers)

# Output:
# True




#------------------------------------------------------------------------------------------------#
# Structure-9: Using "in" with a Dictionary
# <key> in <dictionary>
#------------------------------------------------------------------------------------------------#

# Example-9
student = {
    "name": "Rahim",
    "age": 20,
    "marks": 85
}

print("name" in student)

# Output:
# True




#------------------------------------------------------------------------------------------------#
# Structure-10: Using "not in" with a Dictionary
# <key> not in <dictionary>
#------------------------------------------------------------------------------------------------#

# Example-10
student = {
    "name": "Rahim",
    "age": 20,
    "marks": 85
}

print("address" not in student)

# Output:
# True