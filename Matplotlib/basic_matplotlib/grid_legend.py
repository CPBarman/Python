#================================================================================================#
#                                       Basic Line Plot
#------------------------------------------------------------------------------------------------#
# Grid & Legend:
# 1. plt.grid()
# 2. plt.legend()
#
# Display:
# 3. plt.show()
#
#================================================================================================#




#================================================================================================#
# Structure-1: Grid
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
# Structure-2: Legend
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

