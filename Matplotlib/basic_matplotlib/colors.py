#================================================================================================#
#                                Line Plot Customization

#
# 1. linestyle    → Changes the style of the line
# 2. marker       → Adds markers to data points
# 3. color        → Changes the color of the line
# 4. linewidth    → Changes the thickness of the line
# 5. markersize   → Changes the size of markers
#================================================================================================#




#================================================================================================#
# Structure-1: Color
#------------------------------------------------------------------------------------------------#
# color
#
# Statement:
# The color parameter is used to change the color
# of a line in a plot.
#
# Structure:
# plt.plot(x, y, color="color")
#
# Common Colors:
#
# "red"    → Red
# "blue"   → Blue
# "green"  → Green
# "black"  → Black
# "orange" → Orange
# "purple" → Purple
#================================================================================================#

#Example-1: Basic Color
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y, color="red")
plt.show()

#Example-2: Different Basic Colors
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]
plt.plot(x, y1, color="blue")
plt.plot(x, y2, color="green")
plt.show()

#Example-3: Basic color
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y, c="purple")
plt.show()

#Example-4: Hexadecimal Color
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y, color="#FF5733")
plt.show()

#Example-5: Color Customization
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y, c="purple")
plt.show()

#Example-
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y, color="blue", marker="o", linestyle="--")
plt.show()
