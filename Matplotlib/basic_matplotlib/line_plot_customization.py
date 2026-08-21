#================================================================================================#
#                            PART-3: Line Plot Customization

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