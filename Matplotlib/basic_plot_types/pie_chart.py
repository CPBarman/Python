#================================================================================================#
#                                           Pie Chart
#------------------------------------------------------------------------------------------------#
#
# plt.pie(data)
# → Creates a pie chart
#
# labels
# → Displays category names
#
# autopct
# → Displays percentage values
#
# explode
# → Separates/highlights selected sections
#================================================================================================#




#================================================================================================#
# Structure-4: Pie Chart
#------------------------------------------------------------------------------------------------#
# plt.pie(data)
#
# Statement:
# The plt.pie() function is used to create a pie chart.
#
# A pie chart is used to represent the proportion or
# percentage of different categories within a whole.
#
# Structure:
# plt.pie(data)
#
# data → Numerical values of different categories
#================================================================================================#

#Example-1:
import matplotlib.pyplot as plt

subjects = ["Physics", "Math", "Python", "Chemistry"]
marks = [30, 25, 20, 25]

plt.pie(marks)

plt.show()


#================================================================================================#
# Structure-5: Pie Chart with Labels
#------------------------------------------------------------------------------------------------#
# plt.pie(data, labels=labels)
#
# Statement:
# The labels parameter is used to display the names
# of different categories on the pie chart.
#
# Structure:
# plt.pie(data, labels=labels)
#================================================================================================#

#Example-1
import matplotlib.pyplot as plt

subjects = ["Physics", "Math", "Python", "Chemistry"]
marks = [30, 25, 20, 25]

plt.pie(marks, labels=subjects)

plt.show()


#================================================================================================#
# Structure-3: Display Percentage
#------------------------------------------------------------------------------------------------#
# plt.pie(data, autopct="%.1f%%")
#
# Statement:
# The autopct parameter is used to display the percentage
# value of each section of the pie chart.
#
# Structure:
# plt.pie(data, autopct="%.1f%%")
#================================================================================================#

import matplotlib.pyplot as plt

subjects = ["Physics", "Math", "Python", "Chemistry"]
marks = [30, 25, 20, 25]

plt.pie(
    marks,
    labels=subjects,
    autopct="%.1f%%"
)

plt.show()


#================================================================================================#
# Structure-7: Explode
#------------------------------------------------------------------------------------------------#
# plt.pie(data, explode=explode)
#
# Statement:
# The explode parameter is used to separate one or more
# sections from the center of the pie chart.
#
# Structure:
# plt.pie(data, explode=explode)
#================================================================================================#

import matplotlib.pyplot as plt

subjects = ["Physics", "Math", "Python", "Chemistry"]
marks = [30, 25, 20, 25]

explode = [0.1, 0, 0, 0]

plt.pie(
    marks,
    labels=subjects,
    explode=explode,
    autopct="%.1f%%"
)

plt.show()