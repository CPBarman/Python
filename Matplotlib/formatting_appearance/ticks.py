#================================================================================================#
#                                            Ticks
#------------------------------------------------------------------------------------------------#


#================================================================================================#



#================================================================================================#
# Structure-1: X-axis Ticks
#------------------------------------------------------------------------------------------------#
# plt.xticks()
#
# Statement:
# The plt.xticks() function is used to control the
# positions of tick marks on the X-axis.
#
# Structure:
# plt.xticks(values)
#
# values → Positions of X-axis ticks
#================================================================================================#

#Example-1:
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)

plt.xticks([1, 2, 3, 4, 5])

plt.show()


#================================================================================================#
# Structure-2: Y-axis Ticks
#------------------------------------------------------------------------------------------------#
# plt.yticks()
#
# Statement:
# The plt.yticks() function is used to control the
# positions of tick marks on the Y-axis.
#
# Structure:
# plt.yticks(values)
#
# values → Positions of Y-axis ticks
#================================================================================================#

#Example-1: 
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)

plt.yticks([0, 2, 4, 6, 8, 10])

plt.show()


#================================================================================================#
# Structure-3: Custom Tick Labels
#------------------------------------------------------------------------------------------------#
# plt.xticks()
# plt.yticks()
#
# Statement:
# Custom tick labels are used to replace the default
# numerical tick labels with meaningful text.
#
# Structure:
# plt.xticks(positions, labels)
# plt.yticks(positions, labels)
#
# positions → Position of the tick
# labels    → Text displayed at that position
#================================================================================================#

#Example-1: Custom X-axis Labels
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

plt.plot(x, y)

plt.xticks(
    [1, 2, 3, 4],
    ["Jan", "Feb", "Mar", "Apr"]
)

plt.show()


#================================================================================================#
# Structure-4: Custom Y-axis Tick Labels
#------------------------------------------------------------------------------------------------#
# plt.yticks(positions, labels)
#
# Statement:
# The plt.yticks() function can be used to replace
# numerical Y-axis ticks with custom text labels.
#================================================================================================#

#Example-2: Custom Y-axis Labels
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [1, 2, 3, 4]

plt.plot(x, y)

plt.yticks(
    [1, 2, 3, 4],
    ["Low", "Medium", "High", "Very High"]
)

plt.show()

