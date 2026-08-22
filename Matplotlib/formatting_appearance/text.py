#================================================================================================#
#                                            Text
#------------------------------------------------------------------------------------------------#


#================================================================================================#



#================================================================================================#
# Structure-1: Text on Plot
#------------------------------------------------------------------------------------------------#
# plt.text()
#
# Statement:
# The plt.text() function is used to place custom text
# at a specific position inside a plot.
#
# Structure:
# plt.text(x, y, "text")
#
# x    → X-coordinate of the text
# y    → Y-coordinate of the text
# text → Text to be displayed
#================================================================================================#

#Example-1: Basic Text
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)

plt.text(3, 6, "Important Point")

plt.show()

#================================================================================================#
# Structure-2: Formatted Text
#------------------------------------------------------------------------------------------------#
# plt.text(x, y, "text", fontsize=value)
#
# Statement:
# The fontsize parameter is used to control the size
# of the text.
#
# Structure:
# plt.text(x, y, "text", fontsize=value)
#================================================================================================#

#Example:
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)

plt.text(3, 6, "Important Point", fontsize=14)

plt.show()

#================================================================================================#
# Structure-3: Text Alignment
#------------------------------------------------------------------------------------------------#
# ha → Horizontal Alignment
# va → Vertical Alignment
#
# Structure:
# plt.text(x, y, "text", ha="center", va="center")
#
# ha → "left", "center", "right"
# va → "top", "center", "bottom"
#================================================================================================#

#Example-1:
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)

plt.text(
    3,
    6,
    "Important Point",
    ha="center",
    va="center"
)

plt.show()
