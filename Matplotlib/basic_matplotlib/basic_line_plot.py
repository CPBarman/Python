#================================================================================================#
#                                       Basic Line Plot
#------------------------------------------------------------------------------------------------#
# Plotting:
# 1. plt.plot()

# Display:
# 2. plt.show()
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


