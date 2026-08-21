#================================================================================================#
#                              PART-4: Multiple Plots
#================================================================================================#




#================================================================================================#
# Structure-1: Multiple Lines
#------------------------------------------------------------------------------------------------#
# plt.plot(x, y1)
# plt.plot(x, y2)
#
# Statement:
# Multiple lines can be plotted on the same graph by using
# plt.plot() multiple times.
#
# This is useful for comparing two or more datasets
# on the same graph.
#
# Structure:
# plt.plot(x, y1, label="Data 1")
# plt.plot(x, y2, label="Data 2")
# plt.legend()
#================================================================================================#

#Example-1:
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]
plt.plot(x, y1, label="Data 1")
plt.plot(x, y2, label="Data 2")
plt.legend()
plt.show()


#Example-2:
import matplotlib.pyplot as plt
year = [2022, 2023, 2024, 2025]
student_A = [60, 65, 72, 80]
student_B = [55, 68, 70, 85]
plt.plot(year, student_A, label="Student A")
plt.plot(year, student_B, label="Student B")
plt.xlabel("Year")
plt.ylabel("Marks")
plt.title("Student Performance")
plt.legend()
plt.grid()
plt.show()