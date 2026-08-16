#------------------------------------------------------------------------------------------------#
# Structure-1: Creating a List
# <list_name> = [value1, value2, value3, ...]
#------------------------------------------------------------------------------------------------#

#Example-1
numbers = [10, 20, 30, 40, 50]
print(numbers)         #10, 20, 30, 40, 50

#Example-2
cars= ["Ford", "Volvo", "BMW"]
print(cars)

#Example-3
numbers = [10, 20, 30, 40, 50]
print(numbers[0])      #10

#Example-4
numbers = [10, 20, 30, 40, 50]
print(numbers[0])      #10
print(numbers[1])      #20
print(numbers[2])      #30

#Example-5
cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)


#------------------------------------------------------------------------------------------------#
# Structure-2: Accessing List Elements Using Negative Index
# <list_name> = [value1, value2, value3, ...]
# <list_name>[-<index>]
#------------------------------------------------------------------------------------------------#

# Example-1
numbers = [10, 20, 30, 40, 50]
print(numbers[-1])     #50
print(numbers[-2])     #40


#------------------------------------------------------------------------------------------------#
# Structure-3: Updating a List Element
# <list_name> = [value1, value2, value3, ...]
# <list_name>[<index>] = <new_value>
#------------------------------------------------------------------------------------------------#

# Example-1
numbers = [10, 20, 30, 40, 50]
numbers[2] = 100
print(numbers)      #[10, 20, 100, 40, 50]




#------------------------------------------------------------------------------------------------#
# Structure-4: Adding an Element Using append()
# <list_name> = [value1, value2, value3, ...]
# <list_name>.append(<value>)
#------------------------------------------------------------------------------------------------#

#Example-1
numbers = [10, 20, 30]
numbers.append(40)
print(numbers)         #[10, 20, 30, 40]

#Example-2
cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")
print(cars)

#------------------------------------------------------------------------------------------------#
# Structure-5: Adding an Element Using insert()
# <list_name>.insert(<index>, <value>)
#------------------------------------------------------------------------------------------------#

#Example-1
numbers = [10, 20, 30]
numbers.insert(1, 15)
print(numbers)          #[10, 15, 20, 30]

#------------------------------------------------------------------------------------------------#
# Structure-6: Adding Multiple Elements Using extend()
# <list_name>.extend(<iterable>)
#------------------------------------------------------------------------------------------------#

# Example-1
numbers = [10, 20, 30]
numbers.extend([40, 50, 60])
print(numbers)        #[10, 20, 30, 40, 50, 60]



#------------------------------------------------------------------------------------------------#
# Structure-7: Removing an Element Using remove()
# <list_name>.remove(<value>)
#------------------------------------------------------------------------------------------------#

# Example-1
numbers = [10, 20, 30, 40, 50]
numbers.remove(30)
print(numbers)             #[10, 20, 40, 50]


#------------------------------------------------------------------------------------------------#
# Structure-8: Removing an Element Using pop()
# <list_name>.pop(<index>)
#------------------------------------------------------------------------------------------------#

# Example-1
numbers = [10, 20, 30, 40, 50]
numbers.pop(2)
print(numbers)      #[10, 20, 40, 50]


#------------------------------------------------------------------------------------------------#
# Structure-9: Removing an Element Using del
# del <list_name>[<index>]
#------------------------------------------------------------------------------------------------#

# Example-1
numbers = [10, 20, 30, 40, 50]
del numbers[1]
print(numbers)        #[10, 30, 40, 50]


#------------------------------------------------------------------------------------------------#
# Structure-10: Removing All Elements Using clear()
# <list_name>.clear()
#------------------------------------------------------------------------------------------------#

# Example-1
numbers = [10, 20, 30, 40, 50]
numbers.clear()
print(numbers)           #[]


#------------------------------------------------------------------------------------------------#
# Structure-11: Finding the Length of a List Using len()
# len(<list_name>)
#------------------------------------------------------------------------------------------------#

# Example-1
numbers = [10, 20, 30, 40, 50]
print(len(numbers))

#Example-2
cars = ["Ford", "Volvo", "BMW"]
x = len(cars)
print(x)


# ------------------------------------------------------------------------------------------------#
# Structure-12: Copying a List Using copy()
# <new_list> = <old_list>.copy()
#------------------------------------------------------------------------------------------------#

# Example-1
numbers = [10, 20, 30, 40, 50]
new_numbers = numbers.copy()
print(new_numbers)           #[10, 20, 30, 40, 50]


# Example-2: Modifying the Copied List
numbers = [10, 20, 30]
new_numbers = numbers.copy()
new_numbers.append(40)
print("Original List:", numbers)
print("Copied List:", new_numbers)


#------------------------------------------------------------------------------------------------#
# Structure-13: Counting an Element Using count()
# <list_name>.count(<value>)
#------------------------------------------------------------------------------------------------#

# Example-1
numbers = [10, 20, 10, 30, 10, 40]
print(numbers.count(10))           #3


# Example-2: Counting an Element in a String List
fruits = ["apple", "banana", "apple", "cherry", "apple"]
print(fruits.count("apple"))       #3


#------------------------------------------------------------------------------------------------#
# Structure-14: Finding the Index of an Element Using index()
# <list_name>.index(<value>)
#------------------------------------------------------------------------------------------------#

# Example-1
numbers = [10, 20, 30, 40, 50]
print(numbers.index(30))            #2

#------------------------------------------------------------------------------------------------#
# Structure-15: Reversing a List Using reverse()
# <list_name>.reverse()
#------------------------------------------------------------------------------------------------#

# Example-1
numbers = [10, 20, 30, 40, 50]
numbers.reverse()
print(numbers)             #[50, 40, 30, 20, 10]


# Example-2: Reversing a List of Strings
fruits = ["apple", "banana", "cherry", "mango"]
fruits.reverse()
print(fruits)             #['mango', 'cherry', 'banana', 'apple']


#------------------------------------------------------------------------------------------------#
# Structure-16: Sorting a List Using sort()
# <list_name>.sort()
#------------------------------------------------------------------------------------------------#

# Example-1: Sorting Numbers
numbers = [50, 20, 40, 10, 30]
numbers.sort()
print(numbers)        #[10, 20, 30, 40, 50]

