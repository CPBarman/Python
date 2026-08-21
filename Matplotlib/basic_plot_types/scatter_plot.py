#================================================================================================#
#                                           Scatter Plots
#================================================================================================#




#================================================================================================#
# Structure-3: Scatter Plot
#------------------------------------------------------------------------------------------------#
# plt.scatter(x, y)
#
# Statement:
# The plt.scatter() function is used to create a scatter plot.
#
# A scatter plot displays individual data points on a graph
# and is mainly used to show the relationship between
# two numerical variables.
#
# Structure:
# plt.scatter(x, y)
#
# x → Values for the X-axis
# y → Values for the Y-axis
#================================================================================================#

#Example-1: 
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.scatter(x, y)
plt.show()

#================================================================================================#
# Structure-2: Scatter Plot with Labels and Title
#------------------------------------------------------------------------------------------------#
# plt.scatter()
# plt.xlabel()
# plt.ylabel()
# plt.title()
#
# Statement:
# Labels and a title can be added to a scatter plot
# to make the relationship between variables easier
# to understand.
#================================================================================================#

import matplotlib.pyplot as plt

height = [150, 155, 160, 165, 170, 175, 180]
weight = [50, 53, 56, 60, 64, 68, 72]

plt.scatter(height, weight)

plt.xlabel("Height (cm)")
plt.ylabel("Weight (kg)")
plt.title("Height vs Weight")

plt.show()



#================================================================================================#
# Structure-6: Scatter Point Size
#------------------------------------------------------------------------------------------------#
# plt.scatter(x, y, s=value)
#
# Statement:
# The s parameter is used to change the size of
# scatter points.
#
# Structure:
# plt.scatter(x, y, s=value)
#================================================================================================#

#Example-1
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.scatter(x, y, s=100)

plt.show()
