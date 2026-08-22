#================================================================================================#
#                                            Axes Limits
#------------------------------------------------------------------------------------------------#


#================================================================================================#


#================================================================================================#
# Structure-1: X-axis Limits
#------------------------------------------------------------------------------------------------#
# plt.xlim()
#
# Statement:
# The plt.xlim() function is used to set the visible
# range of values on the X-axis.
#
# Structure:
# plt.xlim(min, max)
#
# min → Minimum X-axis value
# max → Maximum X-axis value
#================================================================================================#

#Example-1
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)

plt.xlim(1, 5)

plt.show()

#================================================================================================#
# Structure-2: Y-axis Limits
#------------------------------------------------------------------------------------------------#
# plt.ylim()
#
# Statement:
# The plt.ylim() function is used to set the visible
# range of values on the Y-axis.
#
# Structure:
# plt.ylim(min, max)
#
# min → Minimum Y-axis value
# max → Maximum Y-axis value
#================================================================================================#

#Example-1
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)

plt.ylim(0, 12)

plt.show()


#Example-2: X & Y Limit 
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)

plt.xlim(0, 6)
plt.ylim(0, 12)

plt.show()
