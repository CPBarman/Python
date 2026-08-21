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
# Structure-1: Line Style
#------------------------------------------------------------------------------------------------#
# linestyle
#
# Statement:
# The linestyle parameter is used to change the style
# or pattern of the line in a plot.
#
# Structure:
# plt.plot(x, y, linestyle="style")
#
# Common Line Styles:
#
# "-"   → Solid line
# "--"  → Dashed line
# ":"   → Dotted line
# "-."  → Dash-dot line
#================================================================================================#

#Example-1: Solid Line
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y, linestyle="-")
plt.show()

#Example-2: Dashed Line
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y, linestyle="--")
plt.show()

#Example-3: Dotted Line
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y, linestyle=":")
plt.show()

#Example-4: Dash-dot Line
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y, linestyle="-.")
plt.show()



#================================================================================================#
# Structure-2: Marker
#------------------------------------------------------------------------------------------------#
# marker
#
# Statement:
# The marker parameter is used to display a symbol
# at each data point in a plot.
#
# Structure:
# plt.plot(x, y, marker="symbol")
#
# Common Markers:
#
# "o" → Circle
# "s" → Square
# "^" → Triangle
# "*" → Star
# "x" → X
#================================================================================================#

#Example-1: Circle Marker
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y, marker="*")
plt.show()

#Example-2: Square Marker
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y, marker="o")
plt.show() 

#Example-3: Triangle Marker
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y, marker="^")
plt.show()

#Example-4: Star Marker
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y, marker="*")
plt.show()

#Example-5: X Marker
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y, marker="x")
plt.show()

#Example-6: Marker with Line Style
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y, marker="o", linestyle="--")
plt.show()


#================================================================================================#
# Structure-3: Color
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
plt.plot(
    x,
    y,
    color="blue",
    marker="o",
    linestyle="--"
)
plt.show()


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