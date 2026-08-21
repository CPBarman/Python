#================================================================================================#
#                                  Basic Line Plot

# Plotting:
# 1. plt.plot()
#
# Labels & Title:
# 2. plt.xlabel()
# 3. plt.ylabel()
# 4. plt.title()
#
# Grid & Legend:
# 5. plt.grid()
# 6. plt.legend()
#
# Display:
# 7. plt.show()
#
#================================================================================================#




#================================================================================================#
# Structure-1: Basic Line Plot
#------------------------------------------------------------------------------------------------#
# plt.plot(x, y)
#
# Statement:
# The plt.plot() function is used to create a line plot
# by connecting data points with straight lines.
#
# Structure:
# plt.plot(x, y)
#
# x → Values for the X-axis
# y → Values for the Y-axis
#================================================================================================#

#Example
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.show()


#================================================================================================#
# Structure-2: X-axis Label
#------------------------------------------------------------------------------------------------#
# plt.xlabel("label")
#
# Statement:
# The plt.xlabel() function is used to add a label
# to the X-axis.
#
# Structure:
# plt.xlabel("label")
#================================================================================================#

#Example
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.xlabel("X-axis")
plt.show()


#================================================================================================#
# Structure-3: Plot Title
#------------------------------------------------------------------------------------------------#
# plt.title("title")
#
# Statement:
# The plt.title() function is used to add a title
# to the plot.
#
# Structure:
# plt.title("title")
#================================================================================================#

#Example
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.title("Basic Line Plot")
plt.show()


#================================================================================================#
# Structure-4: Grid
#------------------------------------------------------------------------------------------------#
# plt.grid()
#
# Statement:
# The plt.grid() function is used to display grid lines
# on the plot.
#
# Structure:
# plt.grid()
#================================================================================================#

#Example-1
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y)
plt.grid()
plt.show()


#================================================================================================#
# Structure-6: Legend
#------------------------------------------------------------------------------------------------#
# plt.legend()
#
# Statement:
# The plt.legend() function is used to display the legend
# for the plotted data.
#
# A legend helps identify different lines or data series
# in a graph.
#
# Structure:
# plt.plot(x, y, label="label")
# plt.legend()
#================================================================================================#

#Example-1
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y, label="y = 2x")
plt.legend()
plt.show()

