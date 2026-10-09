import csv
from tkinter.font import names

with open("Book(Sheet1).csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)




import csv

with open("students.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row[0])




#-------------------------------------Graphical Representation of CSV Data------------------------#


import csv
import matplotlib.pyplot as plt

Name = []
Age = []

with open("Book(Sheet1).csv", "r", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        Name.append(row["Name"])
        Age.append(int(row["Age"]))

plt.bar(Name, Age)

plt.xlabel("Name")
plt.ylabel("Age")
plt.title("Students' Ages")

plt.show()