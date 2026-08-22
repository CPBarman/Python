#================================================================================================#
#                                Line Plot Customization

#
# 1. linestyle    → Changes the style of the line
# 2. marker       → Adds markers to data points
# 3. color        → Changes the color of the line
# 4. linewidth    → Changes the thickness of the line
# 5. markersize   → Changes the size of markers
#
#================================================================================================#




#================================================================================================#
# Structure-4: Line Width
#------------------------------------------------------------------------------------------------#
# linewidth
#
# Statement:
# The linewidth parameter is used to change the thickness
# of a line in a plot.
#
# Structure:
# plt.plot(x, y, linewidth=value)
#
# The default linewidth is generally 1.5.
# A larger value makes the line thicker.
#================================================================================================#

#Example-1
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y, linewidth=3)
plt.show()


#================================================================================================#
# Structure-5: Marker Size
#------------------------------------------------------------------------------------------------#
# markersize
#
# Statement:
# The markersize parameter is used to change the size
# of markers at the data points.
#
# Structure:
# plt.plot(x, y, marker="o", markersize=value)
#
# A larger value makes the marker larger.
#================================================================================================#

#Example-1:
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y, marker="o", markersize=10)
plt.show()