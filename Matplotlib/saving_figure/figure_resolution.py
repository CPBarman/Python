#================================================================================================#
#                             Common File Formats
#------------------------------------------------------------------------------------------------#
#
# PNG
# plt.savefig("plot.png")
#
# JPG
# plt.savefig("plot.jpg")
#
# PDF
# plt.savefig("plot.pdf")
#
# SVG
# plt.savefig("plot.svg")
#
#================================================================================================#





#================================================================================================#
# Structure-1: Figure Resolution
#------------------------------------------------------------------------------------------------#
# dpi
#
# Statement:
# DPI (Dots Per Inch) is used to control the resolution
# or quality of a saved figure.
#
# Structure:
# plt.savefig("filename.png", dpi=value)
#
# dpi → Resolution of the saved figure
#
#================================================================================================#

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)

plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("High Resolution Figure")

plt.savefig("high_resolution_plot.png", dpi=300)

plt.show()



#================================================================================================#
# Structure-2: Removing Extra White Space
#------------------------------------------------------------------------------------------------#
# bbox_inches="tight"
#
# Statement:
# The bbox_inches="tight" parameter is used to reduce
# unnecessary empty space around a saved figure.
#
# Structure:
# plt.savefig("filename.png", bbox_inches="tight")
#
#================================================================================================#

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)

plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Saved Figure")

plt.savefig(
    "my_plot.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


#Complete Example
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.figure(figsize=(8, 5))

plt.plot(x, y, marker="o")

plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Saving a Matplotlib Figure")

plt.grid()

plt.savefig(
    "my_figure.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()