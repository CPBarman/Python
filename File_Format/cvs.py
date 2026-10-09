#================================================================================================#
#                                  CSV Files

# CSV stands for Comma-Separated Values

# A CSV file is a text file used to store tabular data in rows and columns

# Each row represents a record
# Each column represents a field
# Values are usually separated by a comma (,)

# Python provides the built-in "csv" module to work with CSV files
#================================================================================================#




#------------------------------------------------------------------------------------------------#
# Structure-1: Importing the CSV Module
# import csv
#------------------------------------------------------------------------------------------------#

# Example-1
import csv




#------------------------------------------------------------------------------------------------#
# Structure-2: Writing Data to a CSV File
# csv.writer(<file_object>)
#------------------------------------------------------------------------------------------------#

# Example-2
import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Age", "Marks"])
    writer.writerow(["Rahim", 20, 85])
    writer.writerow(["Karim", 21, 90])







#------------------------------------------------------------------------------------------------#
# Structure-3: Writing Multiple Rows to a CSV File
# writer.writerows(<rows>)
#------------------------------------------------------------------------------------------------#

# Example-3
import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    rows = [
        ["Name", "Age", "Marks"],
        ["Rahim", 20, 85],
        ["Karim", 21, 90],
        ["Salma", 20, 95]
    ]

    writer.writerows(rows)




#------------------------------------------------------------------------------------------------#
# Structure-4: Reading Data from a CSV File
# csv.reader(<file_object>)
#------------------------------------------------------------------------------------------------#

# Example-4
import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

# Output:
# ['Name', 'Age', 'Marks']
# ['Rahim', '20', '85']
# ['Karim', '21', '90']
# ['Salma', '20', '95']




#------------------------------------------------------------------------------------------------#
# Structure-5: Reading Each Row and Accessing Individual Values
# <row>[<index>]
#------------------------------------------------------------------------------------------------#

# Example-5
import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row[0], row[2])

# Output:
# Name Marks
# Rahim 85
# Karim 90
# Salma 95




#------------------------------------------------------------------------------------------------#
# Structure-6: Skipping the Header Row
# next(<reader>)
#------------------------------------------------------------------------------------------------#

# Example-6
import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    next(reader)

    for row in reader:
        print(row)

# Output:
# ['Rahim', '20', '85']
# ['Karim', '21', '90']
# ['Salma', '20', '95']




#------------------------------------------------------------------------------------------------#
# Structure-7: Reading a CSV File Using DictReader
# csv.DictReader(<file_object>)
#------------------------------------------------------------------------------------------------#

# Example-7
import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["Name"], row["Marks"])

# Output:
# Rahim 85
# Karim 90
# Salma 95




#------------------------------------------------------------------------------------------------#
# Structure-8: Writing Data Using DictWriter
# csv.DictWriter(<file_object>, fieldnames=<field_names>)
#------------------------------------------------------------------------------------------------#

# Example-8
import csv

with open("students.csv", "w", newline="") as file:
    fieldnames = ["Name", "Age", "Marks"]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({"Name": "Rahim", "Age": 20, "Marks": 85})
    writer.writerow({"Name": "Karim", "Age": 21, "Marks": 90})




#------------------------------------------------------------------------------------------------#
# Structure-9: Appending Data to a CSV File
# open(<file_name>, "a", newline="")
#------------------------------------------------------------------------------------------------#

# Example-9
import csv

with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Salma", 20, 95])




#------------------------------------------------------------------------------------------------#
# Structure-10: Using a Different Delimiter
# csv.reader(<file_object>, delimiter=<delimiter>)
#------------------------------------------------------------------------------------------------#

# Example-10
import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file, delimiter=",")

    for row in reader:
        print(row)

# Output:
# ['Name', 'Age', 'Marks']
# ['Rahim', '20', '85']
# ['Karim', '21', '90']
# ['Salma', '20', '95']