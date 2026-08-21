#================================================================================================#
#                                           Bar Chart
#================================================================================================#




#================================================================================================#
# Structure-1: Bar Chart
#------------------------------------------------------------------------------------------------#
# plt.bar(x, height)
#
# Statement:
# The plt.bar() function is used to create a bar chart.
#
# A bar chart is mainly used to compare values between
# different categories.
#
# Structure:
# plt.bar(x, height)
#
# x      → Categories or X-axis positions
# height → Height of each bar
#================================================================================================#


#Example-1: Basic Bar Chart
import matplotlib.pyplot as plt
subjects = ["Physics", "Math", "Python", "Chemistry"]
marks = [85, 90, 78, 88]
plt.bar(subjects, marks)
plt.show()


#================================================================================================#
# Structure-2: Bar Chart with Labels and Title
#------------------------------------------------------------------------------------------------#
# plt.bar(x, height)
# plt.xlabel()
# plt.ylabel()
# plt.title()
#
# Statement:
# Labels and a title can be added to a bar chart to make
# the data easier to understand.
#================================================================================================#

import matplotlib.pyplot as plt

subjects = ["Physics", "Math", "Python", "Chemistry"]
marks = [85, 90, 78, 88]

plt.bar(subjects, marks)

plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Student Marks")

plt.show()


#================================================================================================#
# Structure-3: Horizontal Bar Chart
#------------------------------------------------------------------------------------------------#
# plt.barh(y, width)
#
# Statement:
# The plt.barh() function is used to create a horizontal
# bar chart.
#
# Structure:
# plt.barh(y, width)
#
# y     → Categories
# width → Width of each bar
#================================================================================================#

#Example: Horizontal Bar Chart
import matplotlib.pyplot as plt

subjects = ["Physics", "Math", "Python", "Chemistry"]
marks = [85, 90, 78, 88]

plt.barh(subjects, marks)

plt.xlabel("Marks")
plt.ylabel("Subjects")
plt.title("Student Marks")

plt.show()

